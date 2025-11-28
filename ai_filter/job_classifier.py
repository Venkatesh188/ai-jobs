"""
AI Job Relevance Classifier
Uses keyword matching to classify job relevance for AI/ML positions.
"""
import logging
import json
from typing import Dict, List, Optional

from config import get_settings, JOB_RELEVANCE_CONFIG


class JobClassifier:
    """
    Classifies job postings for relevance to AI/ML research and engineering roles.
    
    Uses keyword matching to analyze:
    - Job title relevance
    - Job description keywords
    """
    
    def __init__(self):
        """Initialize job classifier."""
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)
        
    def classify_job_relevance(self, job: Dict) -> Dict:
        """
        Classify a single job posting for relevance.
        Uses keyword matching.
        """
        return self._classify_with_keywords(job)

    def _classify_with_keywords(self, job: Dict) -> Dict:
        """
        Classify a single job posting for relevance using keyword matching.
        
        Args:
            job: Job dictionary with keys: title, company, description (optional)
        
        Returns:
            Dictionary with:
            - relevance_score: float (0.0 to 1.0)
            - reasoning: string
            - category: string
            - tags: List[str]
            - is_relevant: bool (score >= min_relevance_score)
        """
        try:
            title = job.get("title", "")
            company = job.get("company", "")
            description = job.get("description", "") or ""
            
            if not title:
                return self._create_rejection_response("Missing job title")

            # Keyword matching logic
            keywords = JOB_RELEVANCE_CONFIG["keywords"]
            excluded = JOB_RELEVANCE_CONFIG["excluded_keywords"]
            
            text = (title + " " + description).lower()
            title_lower = title.lower()
            
            # Check for excluded keywords first
            for word in excluded:
                if word.lower() in title_lower:
                    return {
                        "relevance_score": 0.0,
                        "reasoning": f"Contains excluded keyword in title: {word}",
                        "category": "Other",
                        "tags": [],
                        "is_relevant": False
                    }

            # Calculate score based on keywords
            found_keywords = []
            score = 0.0
            
            # Title matches (high weight)
            for k in keywords:
                if k.lower() in title_lower:
                    found_keywords.append(k)
                    score = max(score, 0.9)
            
            # Description matches (medium weight)
            if score < 0.9:
                for k in keywords:
                    if k.lower() in text:
                        found_keywords.append(k)
                        score = max(score, 0.7)
            
            # Determine category
            category = "Other"
            if any(w in text for w in ["research", "scientist", "paper", "publication"]):
                category = "Research"
            elif any(w in text for w in ["engineer", "developer", "software", "systems"]):
                category = "Engineering"
            elif any(w in text for w in ["data scientist", "analyst"]):
                category = "Data Science"
            elif found_keywords:
                category = "AI/ML"

            is_relevant = score >= self.settings.min_relevance_score
            
            return {
                "relevance_score": score,
                "reasoning": f"Matched keywords: {', '.join(found_keywords[:5])}" if found_keywords else "No relevant keywords found",
                "category": category,
                "tags": found_keywords,
                "is_relevant": is_relevant
            }
        
        except Exception as e:
            self.logger.error(f"Error classifying job: {e}", exc_info=True)
            return self._create_rejection_response(f"Classification error: {str(e)}")

    def _create_rejection_response(self, reason: str) -> Dict:
        """Create a rejection response for irrelevant jobs."""
        return {
            "relevance_score": 0.0,
            "reasoning": reason,
            "category": "Other",
            "tags": [],
            "is_relevant": False
        }
    
    def filter_jobs(self, jobs: List[Dict]) -> List[Dict]:
        """
        Filter a list of jobs based on relevance classification.
        
        Args:
            jobs: List of job dictionaries
        
        Returns:
            List of relevant jobs with added classification metadata
        """
        relevant_jobs = []
        
        self.logger.info(f"Filtering {len(jobs)} jobs using keyword classification")
        
        for job in jobs:
            classification = self.classify_job_relevance(job)
            
            # Add classification metadata to job
            job["classification"] = classification
            
            if classification["is_relevant"]:
                relevant_jobs.append(job)
            else:
                self.logger.debug(
                    f"Filtered out job '{job.get('title', 'N/A')}': "
                    f"score={classification['relevance_score']:.2f}"
                )
        
        self.logger.info(
            f"Filtering complete: {len(relevant_jobs)}/{len(jobs)} jobs relevant "
            f"({len(relevant_jobs)/len(jobs)*100:.1f}% retention)"
        )
        
        return relevant_jobs

