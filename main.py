"""
Main entry point for AI Jobs Scraper.
Orchestrates crawling, filtering, and storage operations.
"""
import asyncio
import logging
from typing import List

from config import get_settings
from crawlers.linkedin_crawler import LinkedInCrawler
from ai_filter.job_classifier import JobClassifier
from data.job_entry import JobEntry, JobStorage
from utils.logger import setup_logging


class ScraperOrchestrator:
    """
    Orchestrates the complete scraping pipeline:
    1. Crawling from multiple sources
    2. AI-based job filtering
    3. Data storage (CSV and Markdown)
    """
    
    def __init__(self):
        """Initialize the orchestrator."""
        self.settings = get_settings()
        self.logger = setup_logging()
        
        # Initialize components
        self.crawlers = []
        self.classifier = JobClassifier()
        self.storage = JobStorage(output_dir=self.settings.output_dir)
        
        # Initialize crawlers
        self._setup_crawlers()
    
    def _setup_crawlers(self):
        """Set up available crawlers."""
        try:
            linkedin_crawler = LinkedInCrawler()
            self.crawlers.append(linkedin_crawler)
            self.logger.info("LinkedIn crawler initialized")
        except Exception as e:
            self.logger.error(f"Error setting up crawlers: {e}", exc_info=True)
    
    async def run_scraping_pipeline(self) -> None:
        """
        Run the complete scraping pipeline.
        
        Steps:
        1. Crawl jobs from all enabled sources
        2. Filter jobs using AI classification
        3. Store jobs in CSV and Markdown formats
        """
        all_jobs = []
        
        try:
            self.logger.info("=" * 60)
            self.logger.info("Starting AI Jobs Scraping Pipeline")
            self.logger.info("=" * 60)
            
            # Step 1: Crawl jobs from all sources
            self.logger.info("Step 1: Crawling jobs from sources...")
            for crawler in self.crawlers:
                try:
                    self.logger.info(f"Crawling from {crawler.source_name}...")
                    
                    # Search for AI/ML jobs
                    search_params = {
                        "keywords": "AI Machine Learning Deep Learning Research Scientist",
                        "location": "",  # All locations
                        "date_posted": "r86400",  # Past 24 hours
                        "max_pages": 1  # Start with 1 page for testing
                    }
                    
                    jobs = await crawler.crawl(search_params=search_params)
                    all_jobs.extend(jobs)
                    
                    self.logger.info(
                        f"Retrieved {len(jobs)} jobs from {crawler.source_name}"
                    )
                    
                except Exception as e:
                    self.logger.error(
                        f"Error crawling {crawler.source_name}: {e}",
                        exc_info=True
                    )
            
            if not all_jobs:
                self.logger.warning("No jobs retrieved from any source")
                return
            
            self.logger.info(f"Total jobs retrieved: {len(all_jobs)}")
            
            # Step 2: Filter jobs using AI classification
            self.logger.info("Step 2: Filtering jobs using AI classification...")
            relevant_jobs = self.classifier.filter_jobs(all_jobs)
            
            if not relevant_jobs:
                self.logger.warning("No relevant jobs found after AI filtering")
                return
            
            self.logger.info(
                f"Relevant jobs after filtering: {len(relevant_jobs)} "
                f"({len(relevant_jobs)/len(all_jobs)*100:.1f}% retention)"
            )
            
            # Step 3: Convert to JobEntry objects
            self.logger.info("Step 3: Processing job entries...")
            job_entries = [
                JobEntry.from_job_dict(job) for job in relevant_jobs
            ]
            
            # Step 4: Store jobs
            self.logger.info("Step 4: Storing jobs...")
            
            if self.settings.csv_output:
                csv_path = self.storage.save_jobs_csv(job_entries)
                self.logger.info(f"Jobs saved to CSV: {csv_path}")
            
            if self.settings.markdown_output:
                md_path = self.storage.save_jobs_markdown(job_entries)
                self.logger.info(f"Jobs saved to Markdown: {md_path}")
            
            self.logger.info("=" * 60)
            self.logger.info("Scraping Pipeline Completed Successfully")
            self.logger.info(f"Total Jobs: {len(job_entries)}")
            self.logger.info("=" * 60)
            
        except Exception as e:
            self.logger.error(f"Error in scraping pipeline: {e}", exc_info=True)
            raise


async def main():
    """Main entry point."""
    orchestrator = ScraperOrchestrator()
    await orchestrator.run_scraping_pipeline()


if __name__ == "__main__":
    asyncio.run(main())

