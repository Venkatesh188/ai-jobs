"""
Configuration management for AI Jobs Scraper.
Handles environment variables, crawler settings, and AI filtering config.
"""
import os
from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # OpenAI Configuration
    openai_api_key: str = Field(default=None, description="OpenAI API key for job filtering")
    
    # Crawler Configuration
    request_delay: float = Field(default=2.0, description="Delay between requests (seconds)")
    max_retries: int = Field(default=3, description="Maximum retry attempts for failed requests")
    timeout: int = Field(default=30, description="Request timeout in seconds")
    
    # Rate Limiting
    respect_robots_txt: bool = Field(default=False, description="Whether to respect robots.txt")
    user_agent: str = Field(
        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        description="User agent string for requests"
    )
    
    # AI Filtering Configuration
    min_relevance_score: float = Field(default=0.7, description="Minimum relevance score for job inclusion")
    
    # Data Storage
    output_dir: str = Field(default="jobs", description="Directory for storing job listings")
    csv_output: bool = Field(default=True, description="Save jobs as CSV")
    markdown_output: bool = Field(default=True, description="Save jobs as Markdown")
    
    # Logging
    log_level: str = Field(default="INFO", description="Logging level")
    log_file: str = Field(default="logs/scraper.log", description="Log file path")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Job Relevance Keywords Configuration
JOB_RELEVANCE_CONFIG = {
    "keywords": [
        "AI", "Artificial Intelligence", "Machine Learning", "ML", 
        "Deep Learning", "Research Scientist", "Data Science", 
        "Computer Vision", "NLP", "Natural Language Processing",
        "Neural Networks", "LLM", "Large Language Models",
        "ML Engineer", "AI Engineer", "ML Researcher"
    ],
    "excluded_keywords": [
        "Sales", "Marketing", "Administrative", "HR",
        "Recruiter", "Account Manager", "Business Development"
    ],
    "required_fields": ["title", "company", "location", "link", "posted_date"]
}


# Crawler Source URLs
CRAWLER_SOURCES = {
    "linkedin": {
        "base_url": "https://www.linkedin.com/jobs/search",
        "enabled": True,
        "rate_limit_delay": 3.0
    },
    "glassdoor": {
        "base_url": "https://www.glassdoor.com/Job/jobs.htm",
        "enabled": False,  # Will be enabled after LinkedIn crawler is stable
        "rate_limit_delay": 3.0
    },
    "indeed": {
        "base_url": "https://www.indeed.com/jobs",
        "enabled": False,  # Will be enabled after LinkedIn crawler is stable
        "rate_limit_delay": 2.0
    },
    "remoteok": {
        "base_url": "https://remoteok.com/api",
        "enabled": True,
        "rate_limit_delay": 1.0
    },
    "weworkremotely": {
        "base_url": "https://weworkremotely.com/categories/remote-programming-jobs.rss",
        "enabled": True,
        "rate_limit_delay": 1.0
    },
    "company_portals": {
        "base_url": "data/companies.json",
        "enabled": True,
        "rate_limit_delay": 1.0
    }
}


def get_settings() -> Settings:
    """Get application settings instance."""
    return Settings()

