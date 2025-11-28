"""
We Work Remotely Job Crawler Implementation
Scrapes job postings from We Work Remotely RSS feed.
"""
import aiohttp
from typing import List, Dict, Optional
from crawlers.base_crawler import BaseCrawler

class WeWorkRemotelyCrawler(BaseCrawler):
    """
    We Work Remotely job crawler implementation.
    Uses the official RSS feed to fetch job listings.
    """
    
    def __init__(self):
        """Initialize We Work Remotely crawler."""
        super().__init__("weworkremotely")
        self.base_url = self.source_config["base_url"]
    
    async def crawl(self, search_params: Optional[Dict] = None) -> List[Dict]:
        """
        Crawl jobs from We Work Remotely RSS feed.
        
        Args:
            search_params: Optional search parameters (ignored for RSS)
            
        Returns:
            List of job dictionaries
        """
        self.logger.info("Starting We Work Remotely crawl...")
        
        try:
            # We Work Remotely has different RSS feeds for categories.
            # We'll fetch the main one or specific categories relevant to AI/Tech.
            # For now, let's use the main remote jobs feed or a specific category if available.
            # The base_url in config should point to the RSS feed.
            
            async with aiohttp.ClientSession() as session:
                headers = {"User-Agent": self.settings.user_agent}
                async with session.get(self.base_url, headers=headers) as response:
                    if response.status != 200:
                        self.logger.error(f"Failed to fetch We Work Remotely RSS: {response.status}")
                        return []
                    
                    content = await response.text()
                    jobs = self.extract_jobs(content)
                    self.logger.info(f"Found {len(jobs)} jobs from We Work Remotely")
                    return jobs
                    
        except Exception as e:
            self.logger.error(f"Error crawling We Work Remotely: {e}", exc_info=True)
            return []

    def extract_jobs(self, raw_data: str) -> List[Dict]:
        """
        Extract structured job data from RSS XML content.
        
        Args:
            raw_data: XML string from RSS feed
            
        Returns:
            List of normalized job dictionaries
        """
        jobs = []
        
        try:
            # Use feedparser if available, otherwise fallback to simple parsing or BS4
            # Since we didn't add feedparser to requirements, let's use BS4 with xml parser
            from bs4 import BeautifulSoup
            
            soup = BeautifulSoup(raw_data, "xml")
            items = soup.find_all("item")
            
            for item in items:
                try:
                    title_full = item.find("title").text if item.find("title") else "N/A"
                    # Title often comes as "Company: Role" or "Role: Company"
                    # WWR format: "Role: Company" or just "Role"
                    
                    description = item.find("description").text if item.find("description") else ""
                    link = item.find("link").text if item.find("link") else ""
                    pub_date = item.find("pubDate").text if item.find("pubDate") else ""
                    
                    # Try to extract company from title if possible, or description
                    # WWR RSS titles are usually "Job Title at Company Name" or "Company Name: Job Title"
                    # Let's assume "Job Title" for now and let the classifier handle it
                    
                    # Check for sponsorship in description
                    sponsorship_info = self._check_sponsorship(description)
                    
                    job = {
                        "title": title_full,
                        "company": "See Title/Desc", # WWR RSS doesn't always separate it cleanly in standard fields
                        "location": "Remote", # It's We Work Remotely
                        "link": link,
                        "posted_date": pub_date,
                        "description": description,
                        "salary": None, # Usually not in RSS metadata
                        "sponsorship_info": sponsorship_info,
                        "source": "weworkremotely",
                        "tags": []
                    }
                    jobs.append(job)
                    
                except Exception as e:
                    self.logger.warning(f"Error extracting job item: {e}")
                    continue
                    
        except Exception as e:
             self.logger.error(f"Error parsing XML: {e}")
             
        return jobs

    def _check_sponsorship(self, description: str) -> Optional[str]:
        """Check description for sponsorship information."""
        if not description:
            return None
            
        desc_lower = description.lower()
        
        negative_phrases = [
            "sponsorship is not available",
            "no sponsorship",
            "cannot sponsor",
            "unable to sponsor",
            "must be authorized to work",
            "us citizens only",
            "green card holders only"
        ]
        
        positive_phrases = [
            "visa sponsorship available",
            "can sponsor",
            "willing to sponsor",
            "sponsorship provided"
        ]
        
        for phrase in negative_phrases:
            if phrase in desc_lower:
                return "Sponsorship likely NOT available"
                
        for phrase in positive_phrases:
            if phrase in desc_lower:
                return "Sponsorship likely available"
                
        return None
