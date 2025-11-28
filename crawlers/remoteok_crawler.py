"""
RemoteOK Job Crawler Implementation
Scrapes job postings from RemoteOK API.
"""
import aiohttp
from typing import List, Dict, Optional
from crawlers.base_crawler import BaseCrawler

class RemoteOKCrawler(BaseCrawler):
    """
    RemoteOK job crawler implementation.
    Uses the official API to fetch job listings.
    """
    
    def __init__(self):
        """Initialize RemoteOK crawler."""
        super().__init__("remoteok")
        self.base_url = self.source_config["base_url"]
    
    async def crawl(self, search_params: Optional[Dict] = None) -> List[Dict]:
        """
        Crawl jobs from RemoteOK API.
        
        Args:
            search_params: Optional search parameters (ignored for now as we fetch feed)
            
        Returns:
            List of job dictionaries
        """
        self.logger.info("Starting RemoteOK crawl...")
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {"User-Agent": self.settings.user_agent}
                async with session.get(self.base_url, headers=headers) as response:
                    if response.status != 200:
                        self.logger.error(f"Failed to fetch RemoteOK API: {response.status}")
                        return []
                    
                    data = await response.json()
                    jobs = self.extract_jobs(data)
                    self.logger.info(f"Found {len(jobs)} jobs from RemoteOK")
                    return jobs
                    
        except Exception as e:
            self.logger.error(f"Error crawling RemoteOK: {e}", exc_info=True)
            return []

    def extract_jobs(self, raw_data: any) -> List[Dict]:
        """
        Extract structured job data from RemoteOK API response.
        
        Args:
            raw_data: List of job objects from API
            
        Returns:
            List of normalized job dictionaries
        """
        jobs = []
        
        # RemoteOK API returns a list where the first item might be legal metadata
        if not isinstance(raw_data, list):
            return []
            
        for item in raw_data:
            # Skip if not a valid job entry
            # RemoteOK uses 'position' for job title
            if not isinstance(item, dict) or "position" not in item or "legal" in item:
                continue
                
            try:
                # Check for sponsorship info in description
                description = item.get("description", "")
                sponsorship_info = self._check_sponsorship(description)
                
                # Format salary
                salary_min = item.get("salary_min")
                salary_max = item.get("salary_max")
                salary = None
                if salary_min or salary_max:
                    salary = f"${salary_min or '?'} - ${salary_max or '?'}"

                job = {
                    "title": item.get("position"),
                    "company": item.get("company"),
                    "location": item.get("location", "Remote"),
                    "link": item.get("apply_url") or item.get("url"),
                    "posted_date": item.get("date"),
                    "description": description,
                    "salary": salary,
                    "sponsorship_info": sponsorship_info,
                    "source": "remoteok",
                    "tags": item.get("tags", [])
                }
                jobs.append(job)
                
            except Exception as e:
                self.logger.warning(f"Error extracting job item: {e}")
                continue
                
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
