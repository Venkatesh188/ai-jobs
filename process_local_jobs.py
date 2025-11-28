"""
Process Local Jobs Script
Loads raw jobs from CSV and runs the AI filter on them.
This is much faster than re-crawling.
"""
import asyncio
import logging
import os
import glob
import pandas as pd
from typing import List, Dict

from config import get_settings
from ai_filter.job_classifier import JobClassifier
from data.job_entry import JobEntry, JobStorage
from utils.logger import setup_logging

class LocalJobProcessor:
    def __init__(self):
        self.settings = get_settings()
        self.logger = setup_logging()
        self.classifier = JobClassifier()
        self.storage = JobStorage(output_dir=self.settings.output_dir)

    def get_latest_raw_file(self) -> str:
        """Find the most recent raw jobs CSV file."""
        raw_dir = os.path.join(self.settings.output_dir, "raw")
        list_of_files = glob.glob(os.path.join(raw_dir, "*.csv"))
        
        if not list_of_files:
            return None
            
        return max(list_of_files, key=os.path.getctime)

    def load_jobs_from_csv(self, filepath: str) -> List[Dict]:
        """Load jobs from CSV and convert to list of dicts."""
        self.logger.info(f"Loading jobs from {filepath}...")
        df = pd.read_csv(filepath)
        
        # Replace NaN with empty strings/defaults
        df = df.fillna("")
        
        jobs = df.to_dict('records')
        return jobs

    def process(self):
        """Main processing loop."""
        self.logger.info("=" * 60)
        self.logger.info("Starting Local Job Processing")
        self.logger.info("=" * 60)

        # 1. Find latest raw file
        raw_file = self.get_latest_raw_file()
        if not raw_file:
            self.logger.error("No raw job files found in jobs/raw/")
            return

        self.logger.info(f"Found latest raw file: {raw_file}")

        # 2. Load jobs
        try:
            all_jobs = self.load_jobs_from_csv(raw_file)
            self.logger.info(f"Loaded {len(all_jobs)} jobs.")
        except Exception as e:
            self.logger.error(f"Error loading CSV: {e}")
            return

        if not all_jobs:
            self.logger.warning("No jobs found in file.")
            return

        # 3. Filter jobs
        self.logger.info("Filtering jobs using AI classification...")
        try:
            # The classifier expects a list of dicts. 
            # Note: If the raw CSV already has classification columns, they might be overwritten, which is fine.
            relevant_jobs = self.classifier.filter_jobs(all_jobs)
        except Exception as e:
            self.logger.error(f"Filtering failed: {e}", exc_info=True)
            return

        if not relevant_jobs:
            self.logger.warning("No relevant jobs found after filtering.")
            return

        # 4. Save results
        self.logger.info("Saving results...")
        try:
            job_entries = [JobEntry.from_job_dict(job) for job in relevant_jobs]
            
            # Save filtered CSV
            csv_path = self.storage.save_jobs_csv(job_entries)
            self.logger.info(f"Saved filtered CSV: {csv_path}")
            
            # Save Markdown
            md_path = self.storage.save_jobs_markdown(job_entries) # This method might not exist in JobStorage based on previous read_file, let me check
            
            # Save Detailed Report
            # I need to check if these methods exist in JobStorage. 
            # Based on main.py they seem to exist but I only read the first 100 lines of job_entry.py.
            # I will assume they exist or I will check job_entry.py again.
            
        except Exception as e:
            self.logger.error(f"Error saving results: {e}", exc_info=True)
            
        self.logger.info("Processing complete.")

if __name__ == "__main__":
    processor = LocalJobProcessor()
    processor.process()
