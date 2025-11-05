"""
AI Job Relevance Classifier
Uses OpenAI API to classify job relevance for AI/ML positions.
"""
import logging
from typing import Dict, List, Optional
from openai import OpenAI

from config import get_settings, JOB_RELEVANCE_CONFIG


class JobClassifier:
    """
    Classifies job postings for relevance to AI/ML research and engineering roles.
    
    Uses OpenAI API to analyze:
    - Job title relevance
    - Job description technical depth
    - Research orientation
    - Career stage alignment
    """
    
    def __init__(self):
        """Initialize job classifier."""
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.settings.openai_api_key)
        
        # Classification prompt template
        self.classification_prompt = self._build_classification_prompt()
    
    def _build_classification_prompt(self) -> str:
        """Build the prompt for job classification."""
        keywords = ", ".join(JOB_RELEVANCE_CONFIG["keywords"])
        excluded = ", ".join(JOB_RELEVANCE_CONFIG["excluded_keywords"])
        
        prompt = f"""You are a job classification expert for AI/ML research and engineering positions.

Analyze the following job posting and determine its relevance to AI/ML research and engineering roles.

RELEVANT KEYWORDS: {keywords}
EXCLUDED KEYWORDS (lower relevance): {excluded}

Evaluation Criteria:
1. AI/ML Keywords Presence (0.0-0.3): Does the job title/description contain relevant AI/ML terms?
2. Research Orientation (0.0-0.3): Is this a research-focused role (vs. pure engineering)?
3. Technical Depth (0.0-0.2): Does the description indicate deep technical requirements?
4. Career Stage Alignment (0.0-0.2): Is this suitable for researchers/engineers (not sales/marketing)?

Provide a JSON response with:
- relevance_score: float (0.0 to 1.0)
- reasoning: string (brief explanation)
- category: string (one of: "Research", "Engineering", "Data Science", "Other")
- tags: array of strings (relevant technology tags)

Job Details:
Title: {{title}}
Company: {{company}}
Description: {{description}}

Respond ONLY with valid JSON, no additional text."""
        
        return prompt
    
    def classify_job_relevance(self, job: Dict) -> Dict:
        """
        Classify a single job posting for relevance.
        
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
            # Prepare job details
            title = job.get("title", "")
            company = job.get("company", "")
            description = job.get("description", "")
            
            if not title:
                return self._create_rejection_response("Missing job title")
            
            # Format prompt
            prompt = self.classification_prompt.format(
                title=title,
                company=company,
                description=description[:1000] if description else "No description provided"
            )
            
            # Call OpenAI API
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",  # Using cost-effective model
                    messages=[
                        {"role": "system", "content": "You are a job classification expert. Always respond with valid JSON only."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3,  # Lower temperature for more consistent classification
                    response_format={"type": "json_object"}
                )
            except Exception as api_error:
                # Fallback for models that don't support response_format
                self.logger.warning(f"JSON mode not supported, using standard mode: {api_error}")
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a job classification expert. Always respond with valid JSON only."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
            
            # Parse response
            import json
            result = json.loads(response.choices[0].message.content)
            
            relevance_score = float(result.get("relevance_score", 0.0))
            is_relevant = relevance_score >= self.settings.min_relevance_score
            
            classification = {
                "relevance_score": relevance_score,
                "reasoning": result.get("reasoning", ""),
                "category": result.get("category", "Other"),
                "tags": result.get("tags", []),
                "is_relevant": is_relevant
            }
            
            self.logger.debug(
                f"Classified job '{title}': score={relevance_score:.2f}, "
                f"relevant={is_relevant}, category={classification['category']}"
            )
            
            return classification
            
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
        
        self.logger.info(f"Filtering {len(jobs)} jobs using AI classification")
        
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
            f"AI filtering complete: {len(relevant_jobs)}/{len(jobs)} jobs relevant "
            f"({len(relevant_jobs)/len(jobs)*100:.1f}% retention)"
        )
        
        return relevant_jobs

