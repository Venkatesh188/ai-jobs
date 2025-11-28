"""
Company Portal Crawler
Scrapes job postings directly from company career pages (Greenhouse, Lever, etc.).
"""
import json
import logging
import aiohttp
from typing import List, Dict, Optional
from datetime import datetime
import os

from crawlers.base_crawler import BaseCrawler

class CompanyCrawler(BaseCrawler):
    """
    Crawler for company career portals.
    Supports Greenhouse and Lever ATS via their public APIs.
    Also supports custom URLs via crawl4ai.
    """
    
    def __init__(self):
        """Initialize Company crawler."""
        super().__init__("company_portals")
        self.companies_file = self.source_config.get("base_url", "data/companies.json")
        self.custom_urls_file = "data/custom_urls.json"
        
    async def crawl(self, search_params: Optional[Dict] = None) -> List[Dict]:
        """
        Crawl configured company portals.
        
        Args:
            search_params: Not used for this crawler
            
        Returns:
            List of job dictionaries
        """
        jobs = []
        
        # Crawl standard companies (Greenhouse/Lever)
        if os.path.exists(self.companies_file):
            try:
                with open(self.companies_file, 'r') as f:
                    companies = json.load(f)
                
                self.logger.info(f"Found {len(companies)} companies to crawl")

                async with aiohttp.ClientSession() as session:
                    for company in companies:
                        try:
                            # Rate limiting
                            self._rate_limited_request()
                            
                            company_jobs = await self._crawl_company(session, company)
                            self.logger.info(f"Found {len(company_jobs)} jobs at {company['name']}")
                            jobs.extend(company_jobs)
                        except Exception as e:
                            self.logger.error(f"Error crawling {company.get('name')}: {e}")
            except Exception as e:
                self.logger.error(f"Error reading companies file: {e}")
        else:
            self.logger.error(f"Companies file not found: {self.companies_file}")

        # Crawl custom URLs
        if os.path.exists(self.custom_urls_file):
            try:
                with open(self.custom_urls_file, 'r') as f:
                    custom_urls = json.load(f)
                
                self.logger.info(f"Found {len(custom_urls)} custom URLs to crawl")
                
                for item in custom_urls:
                    try:
                        custom_jobs = await self._crawl_custom_url(item.get('url'), item.get('name'))
                        self.logger.info(f"Found {len(custom_jobs)} jobs at {item.get('name')} (Custom URL)")
                        jobs.extend(custom_jobs)
                    except Exception as e:
                        self.logger.error(f"Error crawling custom URL {item.get('name')}: {e}")
            except Exception as e:
                self.logger.error(f"Error reading custom URLs file: {e}")
        
        return jobs

    async def _crawl_custom_url(self, url: str, name: str) -> List[Dict]:
        """Crawl a custom URL using crawl4ai."""
        jobs = []
        try:
            from crawl4ai import AsyncWebCrawler
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(url=url)
                
                # Simple heuristic: look for lines with "Apply" or known job titles
                # This is very basic and might need improvement
                if result.markdown:
                    for line in result.markdown.split('\n'):
                        # Basic filtering for potential job titles
                        if any(keyword in line.lower() for keyword in ["engineer", "scientist", "developer", "researcher", "analyst"]):
                            jobs.append({
                                "title": line.strip(),
                                "company": name,
                                "url": url,
                                "description": "Scraped from custom URL",
                                "date_posted": datetime.now().isoformat(),
                                "source": "custom_url"
                            })
        except ImportError:
            self.logger.error("crawl4ai not installed. Cannot crawl custom URLs.")
        except Exception as e:
            self.logger.error(f"Error crawling custom URL {url}: {e}")
        return jobs

    async def _crawl_company(self, session: aiohttp.ClientSession, company: Dict) -> List[Dict]:
        """Crawl a single company portal using its API."""
        board_token = company['id']  # This was 'url' before, now it's the board identifier
        ats = company.get('ats')
        name = company['name']
        
        self.logger.info(f"Fetching jobs for {name} ({ats}) using ID: {board_token}")
        
        try:
            if ats == 'greenhouse':
                return await self._fetch_greenhouse_jobs(session, board_token, name)
            elif ats == 'lever':
                return await self._fetch_lever_jobs(session, board_token, name)
            else:
                self.logger.warning(f"Unknown ATS {ats} for {name}")
                return []
        except Exception as e:
            self.logger.error(f"Request failed for {name}: {e}")
            return []

    async def _fetch_greenhouse_jobs(self, session: aiohttp.ClientSession, board_token: str, company_name: str) -> List[Dict]:
        """Fetch jobs from Greenhouse API."""
        url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
        jobs = []
        
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    self.logger.warning(f"Greenhouse API error for {company_name}: {response.status}")
                    return []
                
                data = await response.json()
                
                for job in data.get('jobs', []):
                    # Greenhouse API with content=true returns the description in 'content'
                    # However, the standard list endpoint might not return full content even with the parameter
                    # We might need to fetch individual job details if content is missing
                    description = job.get('content')
                    
                    # If content is not in the list response, we might need to fetch it individually
                    # But for now, let's try to use what we have or fetch detail if needed.
                    # Based on inspection, the list endpoint DOES NOT return content by default.
                    # We need to fetch individual job details.
                    
                    job_id = job.get('id')
                    if job_id:
                         # Fetch details for each job to get the full description and metadata
                         try:
                             detail_url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs/{job_id}"
                             async with session.get(detail_url) as detail_response:
                                 if detail_response.status == 200:
                                     detail_data = await detail_response.json()
                                     
                                     # Start with the main content
                                     parts = [detail_data.get('content', '')]
                                     
                                     # Add metadata (e.g., Workplace Type, Employment Type)
                                     metadata = detail_data.get('metadata', [])
                                     if metadata:
                                         parts.append("\n\n### Additional Information:")
                                         for item in metadata:
                                             name = item.get('name')
                                             value = item.get('value')
                                             if name and value:
                                                 parts.append(f"- {name}: {value}")
                                     
                                     # Add compliance info if needed, or other fields
                                     
                                     description = "\n".join(filter(None, parts))
                                     
                         except Exception as e:
                             self.logger.warning(f"Failed to fetch details for Greenhouse job {job_id}: {e}")

                    if not description:
                        description = f"Job at {company_name}"

                    jobs.append({
                        "title": job.get('title'),
                        "company": company_name,
                        "location": job.get('location', {}).get('name', 'Remote'),
                        "link": job.get('absolute_url'),
                        "posted_date": job.get('updated_at', datetime.now().isoformat()),
                        "source": "company_portal",
                        "description": description
                    })
        except Exception as e:
            self.logger.error(f"Error fetching Greenhouse jobs for {company_name}: {e}")
            
        return jobs

    async def _fetch_lever_jobs(self, session: aiohttp.ClientSession, board_token: str, company_name: str) -> List[Dict]:
        """Fetch jobs from Lever API."""
        url = f"https://api.lever.co/v0/postings/{board_token}"
        jobs = []
        
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    self.logger.warning(f"Lever API error for {company_name}: {response.status}")
                    return []
                
                data = await response.json()
                
                for job in data:
                    # Construct full description from all available fields
                    parts = []
                    
                    # Opening
                    if job.get('openingPlain'):
                        parts.append(job.get('openingPlain'))
                    elif job.get('opening'):
                        parts.append(job.get('opening'))
                        
                    # Main Description
                    if job.get('descriptionBodyPlain'):
                        parts.append(job.get('descriptionBodyPlain'))
                    elif job.get('descriptionPlain'):
                        parts.append(job.get('descriptionPlain'))
                    elif job.get('description'):
                        parts.append(job.get('description'))
                        
                    # Lists (Requirements, Responsibilities, etc.)
                    lists = job.get('lists', [])
                    if lists:
                        for item in lists:
                            title = item.get('text')
                            content = item.get('content') # This is usually HTML <li>...</li>
                            if title:
                                parts.append(f"\n### {title}")
                            if content:
                                # Simple cleanup if it's HTML list items
                                clean_content = content.replace('<li>', '- ').replace('</li>', '\n')
                                parts.append(clean_content)

                    # Additional Info (Salary, Benefits, etc.)
                    if job.get('additionalPlain'):
                        parts.append("\n### Additional Information")
                        parts.append(job.get('additionalPlain'))
                    elif job.get('additional'):
                        parts.append("\n### Additional Information")
                        parts.append(job.get('additional'))

                    description = "\n\n".join(filter(None, parts))

                    if not description:
                         description = f"Job at {company_name}"
                         
                    jobs.append({
                        "title": job.get('text'),
                        "company": company_name,
                        "location": job.get('categories', {}).get('location', 'Remote'),
                        "link": job.get('hostedUrl'),
                        "posted_date": datetime.fromtimestamp(job.get('createdAt', 0)/1000).isoformat(),
                        "source": "company_portal",
                        "description": description
                    })
        except Exception as e:
            self.logger.error(f"Error fetching Lever jobs for {company_name}: {e}")
            
        return jobs
