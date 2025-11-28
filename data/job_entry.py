"""
Job Entry and Storage Management.
Handles data models and file I/O for job listings.
"""
import csv
import json
import os
import re
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
    salary: str = "Not mentioned"
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
            salary=data.get("salary", "Not mentioned"),
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
            "title", "company", "salary", "location", "posted_date", 
            "link", "source", "relevance_score", "category", 
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

    def update_readme(self, limit: int = 15) -> None:
        """
        Update README.md with the latest jobs from master CSV.
        """
        master_csv = os.path.join(self.output_dir, "master_jobs.csv")
        readme_path = "README.md"
        
        if not os.path.exists(master_csv) or not os.path.exists(readme_path):
            return
            
        try:
            # Read master CSV
            df = pd.read_csv(master_csv)
            
            # Take the last N rows and reverse them (newest first)
            latest_jobs = df.tail(limit).iloc[::-1]
            
            # Create Markdown Table
            table_lines = [
                "| Job Title | Company | Location | Posted | Apply |",
                "|---|---|---|---|---|"
            ]
            
            for _, job in latest_jobs.iterrows():
                title = job.get('title', 'N/A')
                # Escape pipes in title
                title = str(title).replace("|", "-")
                
                company = str(job.get('company', 'N/A')).replace("|", "-")
                location = str(job.get('location', 'N/A')).replace("|", "-")
                posted = str(job.get('posted_date', 'N/A')).replace("|", "-")
                link = job.get('link', '#')
                
                row = f"| **{title}** | {company} | {location} | {posted} | [Apply]({link}) |"
                table_lines.append(row)
                
            table_content = "\n".join(table_lines)
            
            # Update README
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            start_marker = "<!-- JOBS_TABLE_START -->"
            end_marker = "<!-- JOBS_TABLE_END -->"
            
            if start_marker in content and end_marker in content:
                pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
                replacement = f"{start_marker}\n{table_content}\n{end_marker}"
                
                new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    
        except Exception as e:
            print(f"Error updating README: {e}")

    def _write_job_markdown(self, f, job):
        """Helper to write single job to markdown."""
        # Handle both dict and JobEntry object
        if hasattr(job, 'to_dict'):
            job = job.to_dict()
            
        f.write(f"### {job['title']}\n\n")
        f.write(f"- **Company:** {job['company']}\n")
        f.write(f"- **Posted Date:** {job['posted_date']}\n")
        if job.get('salary') and job['salary'] != "Not mentioned":
            f.write(f"- **Salary:** {job['salary']}\n")
        f.write(f"- **Location:** {job['location']}\n")
        f.write(f"- **Application Link:** [Apply Here]({job['link']})\n")
        f.write(f"- **Source:** {job['source']}\n\n")
        f.write("---\n\n")

    def save_detailed_report(self, jobs: List[JobEntry]) -> str:
        """Alias for save_jobs_markdown for now."""
        return self.save_jobs_markdown(jobs)
