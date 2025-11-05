"""
Job Entry Data Model
Defines the structure for job listings and storage operations.
"""
import logging
from datetime import datetime
from typing import List, Optional, Dict
from dataclasses import dataclass, asdict
import csv
import os


@dataclass
class JobEntry:
    """
    Data model for a job posting entry.
    
    Attributes:
        title: Job title
        company: Company name
        location: Job location
        link: URL to job posting
        posted_date: Date job was posted (ISO format)
        source: Source of the job (e.g., 'linkedin', 'glassdoor')
        description: Job description (optional)
        tags: List of relevant tags
        relevance_score: AI classification relevance score
        category: Job category (Research, Engineering, Data Science, etc.)
    """
    title: str
    company: str
    location: str
    link: str
    posted_date: str
    source: str
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    relevance_score: Optional[float] = None
    category: Optional[str] = None
    
    def __post_init__(self):
        """Post-initialization processing."""
        if self.tags is None:
            self.tags = []
        
        # Generate tags if not provided
        if not self.tags:
            self.tags = self._generate_tags()
    
    def _generate_tags(self) -> List[str]:
        """
        Automatically generate relevant tags from job title and description.
        
        Returns:
            List of tag strings
        """
        tags = []
        title_lower = self.title.lower()
        desc_lower = (self.description or "").lower()
        
        # Technology tags
        tech_keywords = {
            "machine learning": "#MachineLearning",
            "deep learning": "#DeepLearning",
            "nlp": "#NLP",
            "natural language processing": "#NLP",
            "computer vision": "#ComputerVision",
            "ai": "#AI",
            "artificial intelligence": "#AI",
            "research": "#Research",
            "data science": "#DataScience",
            "llm": "#LLM",
            "large language model": "#LLM",
            "neural network": "#NeuralNetworks"
        }
        
        for keyword, tag in tech_keywords.items():
            if keyword in title_lower or keyword in desc_lower:
                if tag not in tags:
                    tags.append(tag)
        
        # Source tag
        tags.append(f"#{self.source.capitalize()}")
        
        return tags
    
    def to_dict(self) -> Dict:
        """Convert job entry to dictionary."""
        return asdict(self)
    
    def to_markdown_row(self) -> str:
        """
        Convert job entry to markdown table row.
        
        Returns:
            Markdown table row string
        """
        tags_str = " ".join(self.tags) if self.tags else ""
        score_str = f"{self.relevance_score:.2f}" if self.relevance_score else "N/A"
        
        return (
            f"| {self.title} | {self.company} | {self.location} | "
            f"[Apply]({self.link}) | {self.posted_date} | {tags_str} | {score_str} |"
        )
    
    @classmethod
    def from_dict(cls, data: Dict) -> "JobEntry":
        """
        Create JobEntry from dictionary.
        
        Args:
            data: Dictionary with job data
        
        Returns:
            JobEntry instance
        """
        return cls(
            title=data.get("title", ""),
            company=data.get("company", ""),
            location=data.get("location", ""),
            link=data.get("link", ""),
            posted_date=data.get("posted_date", ""),
            source=data.get("source", "unknown"),
            description=data.get("description"),
            tags=data.get("tags", []),
            relevance_score=data.get("relevance_score"),
            category=data.get("category")
        )
    
    @classmethod
    def from_job_dict(cls, job_dict: Dict) -> "JobEntry":
        """
        Create JobEntry from crawler job dictionary.
        Handles classification metadata if present.
        
        Args:
            job_dict: Job dictionary from crawler/classifier
        
        Returns:
            JobEntry instance
        """
        classification = job_dict.get("classification", {})
        
        return cls(
            title=job_dict.get("title", ""),
            company=job_dict.get("company", ""),
            location=job_dict.get("location", ""),
            link=job_dict.get("link", ""),
            posted_date=job_dict.get("posted_date", ""),
            source=job_dict.get("source", "unknown"),
            description=job_dict.get("description"),
            tags=classification.get("tags", []),
            relevance_score=classification.get("relevance_score"),
            category=classification.get("category")
        )


class JobStorage:
    """
    Handles storage of job entries in CSV and Markdown formats.
    """
    
    def __init__(self, output_dir: str = "jobs"):
        """
        Initialize job storage.
        
        Args:
            output_dir: Directory for storing job files
        """
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
    
    def save_jobs_csv(self, jobs: List[JobEntry], filename: Optional[str] = None) -> str:
        """
        Save jobs to CSV file.
        
        Args:
            jobs: List of JobEntry objects
            filename: Optional filename (default: auto-generated)
        
        Returns:
            Path to saved CSV file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"jobs_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                if not jobs:
                    self.logger.warning("No jobs to save")
                    return filepath
                
                fieldnames = [
                    "title", "company", "location", "link", "posted_date",
                    "source", "tags", "relevance_score", "category"
                ]
                
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for job in jobs:
                    row = job.to_dict()
                    # Convert tags list to string
                    row["tags"] = ", ".join(row.get("tags", []))
                    writer.writerow(row)
            
            self.logger.info(f"Saved {len(jobs)} jobs to CSV: {filepath}")
            return filepath
            
        except Exception as e:
            self.logger.error(f"Error saving CSV: {e}", exc_info=True)
            raise
    
    def save_jobs_markdown(self, jobs: List[JobEntry], 
                          filename: Optional[str] = None) -> str:
        """
        Save jobs to Markdown file with table format.
        
        Args:
            jobs: List of JobEntry objects
            filename: Optional filename (default: auto-generated by date)
        
        Returns:
            Path to saved Markdown file
        """
        if filename is None:
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%B").lower()
            filename = f"{year}/{month}.md"
        
        filepath = os.path.join(self.output_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        try:
            with open(filepath, 'a', encoding='utf-8') as f:
                # Write header if file is new
                if os.path.getsize(filepath) == 0:
                    f.write("# AI Jobs Listings\n\n")
                    f.write(f"*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
                    f.write("| Title | Company | Location | Link | Posted Date | Tags | Relevance Score |\n")
                    f.write("|-------|---------|----------|------|--------------|------|----------------|\n")
                
                # Write job entries
                for job in jobs:
                    f.write(job.to_markdown_row() + "\n")
            
            self.logger.info(f"Saved {len(jobs)} jobs to Markdown: {filepath}")
            return filepath
            
        except Exception as e:
            self.logger.error(f"Error saving Markdown: {e}", exc_info=True)
            raise

