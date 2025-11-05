"""
LinkedIn Job Crawler Implementation
Scrapes AI/ML job postings from LinkedIn.
"""
import time
from typing import List, Dict, Optional
from urllib.parse import urlencode, quote

from crawl4ai import AsyncWebCrawler
from crawlers.base_crawler import BaseCrawler


class LinkedInCrawler(BaseCrawler):
    """
    LinkedIn job crawler implementation.
    
    Note: LinkedIn has strict anti-scraping measures. This crawler
    implements best practices for ethical scraping.
    """
    
    def __init__(self):
        """Initialize LinkedIn crawler."""
        super().__init__("linkedin")
        self.base_url = self.source_config["base_url"]
    
    def _build_search_url(self, keywords: str = "AI Machine Learning", 
                         location: str = "", 
                         date_posted: str = "r86400") -> str:
        """
        Build LinkedIn job search URL.
        
        Args:
            keywords: Search keywords (default: "AI Machine Learning")
            location: Location filter (empty string for all locations)
            date_posted: Date posted filter
                - r86400: Past 24 hours
                - r604800: Past week
                - r2592000: Past month
        
        Returns:
            Complete LinkedIn job search URL
        """
        params = {
            "keywords": keywords,
            "location": location,
            "f_TPR": date_posted,  # Time posted range
            "f_E": "2,3,4",  # Experience level: Mid, Senior, Executive
            "position": "1",  # Full-time
        }
        
        query_string = urlencode(params, doseq=True)
        return f"{self.base_url}?{query_string}"
    
    async def _crawl_page(self, url: str) -> Optional[Dict]:
        """
        Crawl a single LinkedIn job search page.
        
        Args:
            url: URL to crawl
            
        Returns:
            Dictionary with page content or None if failed
        """
        if not self.can_fetch(url):
            self.logger.warning(f"Robots.txt disallows: {url}")
            return None
        
        try:
            self._rate_limited_request()
            
            async with AsyncWebCrawler(verbose=False) as crawler:
                result = await crawler.arun(url=url)
                
                if result.success:
                    return {
                        "html": result.html,
                        "markdown": result.markdown,
                        "url": url
                    }
                else:
                    self.logger.error(f"Failed to crawl {url}: {result.error_message}")
                    return None
                    
        except Exception as e:
            self._handle_errors(e, f"crawling {url}")
            return None
    
    def extract_jobs(self, raw_data: Dict) -> List[Dict]:
        """
        Extract job listings from LinkedIn page HTML.
        
        Args:
            raw_data: Dictionary with HTML content from crawl
            
        Returns:
            List of job dictionaries
        """
        jobs = []
        
        try:
            from bs4 import BeautifulSoup
            
            html = raw_data.get("html", "")
            if not html:
                return jobs
            
            soup = BeautifulSoup(html, "html.parser")
            
            # LinkedIn job listing structure (may need adjustment based on actual HTML)
            job_cards = soup.find_all("div", {"class": "job-search-card"})
            
            for card in job_cards:
                try:
                    # Extract job title
                    title_elem = card.find("h3", {"class": "base-search-card__title"})
                    title = title_elem.get_text(strip=True) if title_elem else "N/A"
                    
                    # Extract company name
                    company_elem = card.find("h4", {"class": "base-search-card__subtitle"})
                    company = company_elem.get_text(strip=True) if company_elem else "N/A"
                    
                    # Extract location
                    location_elem = card.find("span", {"class": "job-search-card__location"})
                    location = location_elem.get_text(strip=True) if location_elem else "N/A"
                    
                    # Extract job link
                    link_elem = card.find("a", {"class": "base-card__full-link"})
                    link = link_elem.get("href", "") if link_elem else ""
                    
                    # Extract posted date
                    date_elem = card.find("time", {"class": "job-search-card__listdate"})
                    posted_date = date_elem.get("datetime", "") if date_elem else ""
                    
                    if title and link:
                        jobs.append({
                            "title": title,
                            "company": company,
                            "location": location,
                            "link": link,
                            "posted_date": posted_date,
                            "source": "linkedin"
                        })
                        
                except Exception as e:
                    self.logger.warning(f"Error extracting job from card: {e}")
                    continue
            
            self.logger.info(f"Extracted {len(jobs)} jobs from LinkedIn")
            
        except Exception as e:
            self._handle_errors(e, "extracting jobs")
        
        return jobs
    
    async def crawl(self, search_params: Optional[Dict] = None) -> List[Dict]:
        """
        Crawl LinkedIn for AI/ML job postings.
        
        Args:
            search_params: Optional dictionary with:
                - keywords: Search keywords (default: "AI Machine Learning")
                - location: Location filter
                - date_posted: Date posted filter
                - max_pages: Maximum pages to crawl (default: 1)
        
        Returns:
            List of job dictionaries
        """
        self.validate_config()
        
        if search_params is None:
            search_params = {}
        
        keywords = search_params.get("keywords", "AI Machine Learning")
        location = search_params.get("location", "")
        date_posted = search_params.get("date_posted", "r86400")
        max_pages = search_params.get("max_pages", 1)
        
        all_jobs = []
        
        try:
            # Build search URL
            search_url = self._build_search_url(keywords, location, date_posted)
            self.logger.info(f"Starting LinkedIn crawl: {search_url}")
            
            # Crawl pages
            for page in range(max_pages):
                page_url = f"{search_url}&start={page * 25}"  # LinkedIn shows 25 jobs per page
                
                self.logger.info(f"Crawling page {page + 1}/{max_pages}")
                
                raw_data = await self._crawl_page(page_url)
                
                if raw_data:
                    jobs = self.extract_jobs(raw_data)
                    all_jobs.extend(jobs)
                else:
                    self.logger.warning(f"Failed to crawl page {page + 1}")
                
                # Additional delay between pages
                if page < max_pages - 1:
                    time.sleep(self.source_config.get("rate_limit_delay", 3.0))
            
            self.logger.info(f"LinkedIn crawl completed: {len(all_jobs)} jobs found")
            
        except Exception as e:
            self._handle_errors(e, "crawling LinkedIn")
        
        return all_jobs

