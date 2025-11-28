import asyncio
import logging
from crawlers.company_crawler import CompanyCrawler
from utils.logger import setup_logging

async def main():
    setup_logging()
    logging.getLogger().setLevel(logging.INFO)
    
    crawler = CompanyCrawler()
    print("Starting Company Crawler...")
    jobs = await crawler.crawl()
    
    print(f"Total jobs found: {len(jobs)}")
    if jobs:
        print("Sample job:")
        print(jobs[0])

if __name__ == "__main__":
    asyncio.run(main())
