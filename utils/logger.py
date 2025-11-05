"""
Logging utilities for the AI Jobs Scraper.
"""
import logging
import os
from pathlib import Path
from config import get_settings


def setup_logging() -> logging.Logger:
    """
    Set up comprehensive logging for the application.
    
    Returns:
        Configured logger instance
    """
    settings = get_settings()
    
    # Create logs directory
    log_dir = os.path.dirname(settings.log_file) or "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Configure root logger
    logger = logging.getLogger("ai_jobs_scraper")
    logger.setLevel(getattr(logging, settings.log_level))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # File handler
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

