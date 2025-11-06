import time
from typing import List, Dict

def scrape_ai_jobs(search_term: str = "artificial intelligence", limit: int = 10) -> List[Dict]:
    """
    Scrape AI job postings from RemoteOK

    Args:
        search_term: Job search keyword (default: "artificial intelligence")
        limit: Maximum number of jobs to return

    Returns:
        List of dictionaries containing job information
    """
    jobs = []

    try:
        # RemoteOK API endpoint
        url = "https://remoteok.com/api"

        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Make request
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()

        # Skip first item (it's metadata)
        job_listings = data[1:] if len(data) > 1 else []

        # Filter for AI-related jobs
        search_terms = search_term.lower().split()

        for job in job_listings:
            # Check if job matches search terms
            job_text = f"{job.get('position', '')} {job.get('description', '')} {job.get('tags', [])}".lower()

            if any(term in job_text for term in search_terms):
                job_info = {
                    'company': job.get('company', 'N/A'),
                    'position': job.get('position', 'N/A'),
                    'location': job.get('location', 'Remote'),
                    'salary': format_salary(job.get('salary_min'), job.get('salary_max')),
                    'apply_url': job.get('url', 'N/A')
                }

                jobs.append(job_info)

                if len(jobs) >= limit:
                    break

        return jobs

    except requests.exceptions.RequestException as e:
        print(f"Error fetching jobs: {e}")
        return []


def format_salary(min_sal, max_sal) -> str:
    """Format salary range into readable string"""
    if min_sal and max_sal:
        return f"${min_sal:,} - ${max_sal:,}"
    elif min_sal:
        return f"${min_sal:,}+"
    elif max_sal:
        return f"Up to ${max_sal:,}"
    else:
        return "Not specified"

# Example usage
if __name__ == "__main__":
    print("Scraping AI job postings…\n")

    # Search for AI/ML jobs
    ai_jobs = scrape_ai_jobs(search_term="artificial intelligence machine learning ai", limit=10)

    # Display results
    for i, job in enumerate(ai_jobs, 1):
        print(f"--- Job {i} ---")
        print(f"Company: {job['company']}")
        print(f"Position: {job['position']}")
        print(f"Location: {job['location']}")
        print(f"Salary: {job['salary']}")
        print(f"Apply: {job['apply_url']}")
        print()

    print(f"Total jobs found: {len(ai_jobs)}")

    # Be respectful - add delay between requests if scraping multiple times
    time.sleep(2)