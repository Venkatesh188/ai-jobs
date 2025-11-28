"""
Scheduler for AI Jobs Scraper.
Runs the scraping pipeline periodically (e.g., every hour).
"""
import asyncio
import logging
import time
from datetime import datetime
import schedule
from main import ScraperOrchestrator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/scheduler.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("scheduler")

def run_job():
    """Wrapper to run the async scraping pipeline synchronously for schedule."""
    logger.info("Starting scheduled scraping job...")
    try:
        # Create a new event loop for each run to avoid closed loop issues
        asyncio.run(run_pipeline())
    except Exception as e:
        logger.error(f"Scheduled job failed: {e}", exc_info=True)

async def run_pipeline():
    """Run the scraping pipeline."""
    orchestrator = ScraperOrchestrator()
    await orchestrator.run_scraping_pipeline()

def main():
    """Main scheduler loop."""
    logger.info("Scheduler started. Job set to run every hour.")
    
    # Run immediately on startup
    run_job()
    
    # Schedule every hour
    schedule.every(1).hours.do(run_job)
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            logger.info("Scheduler stopped by user.")
            break
        except Exception as e:
            logger.error(f"Scheduler loop error: {e}", exc_info=True)
            time.sleep(60)

if __name__ == "__main__":
    main()
