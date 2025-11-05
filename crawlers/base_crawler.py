"""
Base Crawler Abstract Class
Provides common functionality for all job crawlers.
"""
import time
import logging
from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin
import backoff

from config import get_settings, CRAWLER_SOURCES


class BaseCrawler(ABC):
    """
    Abstract base class for all job crawlers.
    
    Provides:
    - Logging setup
    - Rate limiting
    - Robots.txt respect
    - Error handling
    - Retry logic
    """
    
    def __init__(self, source_name: str):
        """
        Initialize base crawler.
        
        Args:
            source_name: Name of the job source (e.g., 'linkedin', 'glassdoor')
        """
        self.source_name = source_name
        self.settings = get_settings()
        self.logger = self._setup_logging()
        self.robot_parser: Optional[RobotFileParser] = None
        
        # Validate source configuration
        if source_name not in CRAWLER_SOURCES:
            raise ValueError(f"Unknown source: {source_name}")
        
        self.source_config = CRAWLER_SOURCES[source_name]
        
        if not self.source_config.get("enabled", False):
            self.logger.warning(f"Source {source_name} is not enabled")
        
        # Setup robots.txt parser
        if self.settings.respect_robots_txt:
            self._setup_robots_parser()
    
    def _setup_logging(self) -> logging.Logger:
        """Set up comprehensive logging for the crawler."""
        logger = logging.getLogger(f"{__name__}.{self.source_name}")
        logger.setLevel(getattr(logging, self.settings.log_level))
        
        # Create logs directory if it doesn't exist
        import os
        os.makedirs(os.path.dirname(self.settings.log_file) or ".", exist_ok=True)
        
        # File handler
        file_handler = logging.FileHandler(self.settings.log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def _setup_robots_parser(self) -> None:
        """Set up robots.txt parser for the source domain."""
        try:
            base_url = self.source_config["base_url"]
            robots_url = urljoin(base_url, "/robots.txt")
            
            self.robot_parser = RobotFileParser()
            self.robot_parser.set_url(robots_url)
            self.robot_parser.read()
            
            self.logger.info(f"Loaded robots.txt from {robots_url}")
        except Exception as e:
            self.logger.warning(f"Could not load robots.txt: {e}")
            self.robot_parser = None
    
    def can_fetch(self, url: str) -> bool:
        """
        Check if URL can be fetched according to robots.txt.
        
        Args:
            url: URL to check
            
        Returns:
            True if URL can be fetched, False otherwise
        """
        if not self.settings.respect_robots_txt or not self.robot_parser:
            return True
        
        return self.robot_parser.can_fetch(self.settings.user_agent, url)
    
    def validate_config(self) -> bool:
        """
        Validate crawler configuration.
        
        Returns:
            True if configuration is valid, raises exception otherwise
        """
        if not self.source_config.get("enabled", False):
            raise ValueError(f"Source {self.source_name} is not enabled")
        
        if not self.source_config.get("base_url"):
            raise ValueError(f"Base URL not configured for {self.source_name}")
        
        self.logger.info(f"Configuration validated for {self.source_name}")
        return True
    
    @backoff.on_exception(
        backoff.expo,
        Exception,
        max_tries=3,
        max_time=300
    )
    def _rate_limited_request(self):
        """Apply rate limiting delay."""
        delay = self.source_config.get("rate_limit_delay", self.settings.request_delay)
        time.sleep(delay)
    
    def _handle_errors(self, error: Exception, context: Optional[str] = None) -> None:
        """
        Centralized error handling and logging.
        
        Args:
            error: Exception that occurred
            context: Additional context about where error occurred
        """
        error_msg = f"Error in {self.source_name} crawler"
        if context:
            error_msg += f" ({context})"
        error_msg += f": {str(error)}"
        
        self.logger.error(error_msg, exc_info=True)
    
    @abstractmethod
    async def crawl(self, search_params: Optional[Dict] = None) -> List[Dict]:
        """
        Abstract method to crawl job listings.
        
        Args:
            search_params: Optional dictionary with search parameters
                (e.g., keywords, location, date_posted)
        
        Returns:
            List of job dictionaries with keys:
            - title: Job title
            - company: Company name
            - location: Job location
            - link: URL to job posting
            - posted_date: Date job was posted
            - description: Job description (optional)
        
        Raises:
            NotImplementedError: Must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement crawl method")
    
    def extract_jobs(self, raw_data: any) -> List[Dict]:
        """
        Extract structured job data from raw crawler response.
        To be implemented by subclasses for source-specific parsing.
        
        Args:
            raw_data: Raw data from crawler
            
        Returns:
            List of job dictionaries
        """
        raise NotImplementedError("Subclasses must implement extract_jobs method")

