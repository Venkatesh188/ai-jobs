"""
Job Entry and Storage Management.
Handles data models and file I/O for job listings.
"""
import csv
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Dict, Optional
import pandas as pd

@dataclass
class JobEntry:
    """Data model for a single job entry."""
    title: str
    company: str
    location: str
    link: str
    posted_date: str
    source: str
    description: str = ""
    relevance_score: float = 0.0
    reasoning: str = ""
    category: str = "Other"
    tags: List[str] = None
    is_relevant: bool = False
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

    @classmethod
    def from_job_dict(cls, data: Dict) -> 'JobEntry':
        """Create JobEntry from dictionary."""
        classification = data.get("classification", {})
        return cls(
            title=data.get("title", ""),
            company=data.get("company", ""),
            location=data.get("location", ""),
            link=data.get("link", ""),
            posted_date=data.get("posted_date", ""),
            source=data.get("source", "unknown"),
            description=data.get("description", ""),
            relevance_score=classification.get("relevance_score", 0.0),
            reasoning=classification.get("reasoning", ""),
            category=classification.get("category", "Other"),
            tags=classification.get("tags", []),
            is_relevant=classification.get("is_relevant", False)
        )
    
    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return asdict(self)


class JobStorage:
    """Handles storage of job entries to CSV and Markdown."""
    
    def __init__(self, output_dir: str = "jobs"):
        self.output_dir = output_dir
        self._ensure_directories()
        
    def _ensure_directories(self):
        """Create necessary directories."""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "raw"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "filtered"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "reports"), exist_ok=True)

    def save_jobs_csv(self, jobs: List[JobEntry], filename: str = None, folder: str = "filtered") -> str:
        """Save jobs to CSV file."""
        if not jobs:
            return ""
            
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"jobs_{timestamp}.csv"
            
        filepath = os.path.join(self.output_dir, folder, filename)
        
        df = pd.DataFrame([job.to_dict() for job in jobs])
        
        # Reorder columns for better readability
        columns = [
            "title", "company", "relevance_score", "category", 
            "location", "posted_date", "source", "link", 
            "reasoning", "tags", "is_relevant"
        ]
        # Add any extra columns that might exist
        existing_cols = [c for c in columns if c in df.columns]
        remaining_cols = [c for c in df.columns if c not in columns and c != "description"]
        
        # Save without description to keep CSV clean, or include it if needed
        # For now, let's exclude description from main CSV to keep it lightweight
        final_cols = existing_cols + remaining_cols
        
        df[final_cols].to_csv(filepath, index=False)
        return filepath

    def save_jobs_master_csv(self, jobs: List[JobEntry]) -> str:
        """Append jobs to master CSV."""
        filepath = os.path.join(self.output_dir, "master_jobs.csv")
        
        new_df = pd.DataFrame([job.to_dict() for job in jobs])
        
        if os.path.exists(filepath):
            existing_df = pd.read_csv(filepath)
            combined_df = pd.concat([existing_df, new_df]).drop_duplicates(subset=["link"])
        else:
            combined_df = new_df
            
        combined_df.to_csv(filepath, index=False)
        return filepath

    def save_jobs_markdown(self, jobs: List[JobEntry]) -> str:
        """Save jobs to Markdown file."""
        if not jobs:
            return ""
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"jobs_report_{timestamp}.md"
        filepath = os.path.join(self.output_dir, "reports", filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# AI Jobs Report - {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write(f"Total Jobs Found: {len(jobs)}\n\n")
            
            # Group by category
            df = pd.DataFrame([job.to_dict() for job in jobs])
            if "category" in df.columns:
                for category, group in df.groupby("category"):
                    f.write(f"## {category} ({len(group)})\n\n")
                    for _, job in group.iterrows():
                        self._write_job_markdown(f, job)
            else:
                for job in jobs:
                    self._write_job_markdown(f, job.to_dict())
                    
        return filepath

    def _write_job_markdown(self, f, job):
        """Helper to write single job to markdown."""
        f.write(f"### [{job['title']}]({job['link']})\n")
        f.write(f"**Company:** {job['company']} | **Location:** {job['location']}\n")
        f.write(f"**Score:** {job['relevance_score']} | **Source:** {job['source']}\n\n")
        f.write(f"> {job['reasoning']}\n\n")
        if job['tags']:
            f.write(f"**Tags:** {', '.join(job['tags'])}\n\n")
        f.write("---\n\n")

    def save_detailed_report(self, jobs: List[JobEntry]) -> str:
        """Alias for save_jobs_markdown for now."""
        return self.save_jobs_markdown(jobs)
