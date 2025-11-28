import pandas as pd
import os
import json
from datetime import datetime

def generate_static_data():
    """
    Reads the master jobs CSV and converts it to a JSON file for the static site.
    """
    # Paths
    jobs_file = os.path.join("jobs", "master_jobs.csv")
    output_dir = "docs"
    output_file = os.path.join(output_dir, "jobs.json")
    
    # Ensure docs directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(jobs_file):
        print(f"Error: {jobs_file} not found. Run the scraper first.")
        # Create a dummy file for demonstration if real data is missing
        print("Creating dummy data for demonstration...")
        data = [
            {
                "title": "Senior AI Engineer",
                "company": "Tech Corp",
                "location": "Remote",
                "url": "#",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "source": "Demo"
            },
            {
                "title": "Machine Learning Researcher",
                "company": "AI Lab",
                "location": "San Francisco, CA",
                "url": "#",
                "date": datetime.now().strftime("%Y-%m-%d"),
                "source": "Demo"
            }
        ]
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Dummy data generated at {output_file}")
        return

    try:
        # Read CSV
        df = pd.read_csv(jobs_file)
        
        # Clean up data (handle NaNs)
        df = df.fillna("")
        
        # Convert to list of dicts
        jobs_data = df.to_dict(orient="records")
        
        # Save to JSON
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(jobs_data, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully generated {output_file} with {len(jobs_data)} jobs.")
        
    except Exception as e:
        print(f"Error generating static data: {e}")

if __name__ == "__main__":
    generate_static_data()
