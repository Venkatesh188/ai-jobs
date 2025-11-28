# AI Jobs Aggregator - Engineering Case Study

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-ETL-green)
![Status](https://img.shields.io/badge/Status-Portfolio_Project-orange)

**A distributed data pipeline for aggregating and normalizing job market data.**

> **Note for Recruiters**: This repository is a **portfolio case study** demonstrating data engineering skills (Web Scraping, ETL, Data Normalization). It is not currently operating as a live commercial service.

##  [Read the Technical Deep Dive (PORTFOLIO.md)](./PORTFOLIO.md)

---

##  Architecture
This project implements a modular ETL pipeline:
1. **Extract**: Crawlers (using Strategy Pattern) fetch data from multiple sources (LinkedIn, RemoteOK, etc.).
2. **Transform**: Data is normalized into a strict schema, cleaned, and deduplicated.
3. **Load**: Processed data is stored in structured formats (CSV/JSON) and visualized via a static dashboard.

##  Key Features
- **Polymorphic Crawlers**: extensible architecture to add new sources easily.
- **Resilience**: Exponential backoff, user-agent rotation, and error handling.
- **Data Quality**: Pydantic-based validation and keyword-based filtering.
- **Static Dashboard**: A lightweight frontend to visualize the aggregated data.

##  Quick Start

### Prerequisites
- Python 3.10+

### Installation
```bash
git clone https://github.com/yourusername/ai-jobs.git
cd ai-jobs
pip install -r requirements.txt
```

### Running the Pipeline
```bash
# 1. Run the scrapers
python main.py

# 2. Generate the static dashboard data
python generate_static_site.py

# 3. View the dashboard
# Open docs/index.html in your browser
```

##  Disclaimer
This software is for educational purposes only. It demonstrates how to architect a data collection pipeline. Users are responsible for adhering to the Terms of Service of any websites they interact with.

