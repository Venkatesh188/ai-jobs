# AI Jobs Aggregator - Engineering Case Study

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-ETL-green)
![Status](https://img.shields.io/badge/Status-Portfolio_Project-orange)

**A distributed data pipeline for aggregating and normalizing job market data.**

> **Note for Recruiters**: This repository is a **portfolio case study** demonstrating data engineering skills (Web Scraping, ETL, Data Normalization). It is not currently operating as a live commercial service.

##  [Read the Technical Deep Dive (PORTFOLIO.md)](./PORTFOLIO.md)

### 🌟 Why This Repo?
- **🛂 Visa Sponsorship Focus**: We prioritize listings that are friendly to international talent.
- **⚡ Hourly Updates**: Our bots run 24/7 to bring you the freshest jobs before anyone else.
- **🤖 Smart Filtering**: We filter out the noise to bring you high-quality AI/ML roles.
- **🔓 100% Open Source**: Built by the community, for the community.

## 📊 Live Job Stats
- **Update Frequency**: Every Hour
- **Focus Domains**: AI, ML, Data Science, Research
- **Key Sources**: LinkedIn, RemoteOK, WeWorkRemotely, and more.

### 🔥 Latest AI Jobs
<!-- JOBS_TABLE_START -->
| Job Title | Company | Location | Posted | Apply |
|---|---|---|---|---|
| **Software Engineer - Core Interfaces** | Palantir | Palo Alto, CA | 2026-01-13T21:22:02.388000 | [Apply](https://jobs.lever.co/palantir/cf76738e-3030-42fa-92ac-a9446df956fc) |
| **Security Controller** | Palantir | London, United Kingdom | 2016-02-24T23:37:05.170000 | [Apply](https://jobs.lever.co/palantir/376064b4-c119-45b5-923d-6ebbb19ec684) |
| **Forward Deployed Software Engineer - US Government** | Palantir | Fayetteville, NC | 2026-01-12T22:44:10.743000 | [Apply](https://jobs.lever.co/palantir/d83fac1c-353e-4b77-a586-3276b1090b6e) |
| **Forward Deployed Software Engineer - Autonomous Systems C2** | Palantir | Palo Alto, CA | 2026-01-16T17:52:11.312000 | [Apply](https://jobs.lever.co/palantir/c62264f5-5da8-40fe-9b44-f7f0f0012e11) |
| **Forward Deployed Software Engineer - Autonomous Systems C2** | Palantir | Seattle, WA | 2026-01-16T17:51:52.386000 | [Apply](https://jobs.lever.co/palantir/0edf7365-49f0-4263-818a-19409ec4f430) |
| **Forward Deployed Infrastructure Engineer - US Government** | Palantir | New York, NY | 2023-09-14T01:23:51.418000 | [Apply](https://jobs.lever.co/palantir/b57f08e9-546c-4b9b-8d21-db0ebbc11363) |
| **Financial Audit Manager** | Palantir | Palo Alto, CA | 2024-07-04T06:55:39.794000 | [Apply](https://jobs.lever.co/palantir/f77d4993-914c-436f-91ef-94f2ee757e40) |
| **Financial Analyst - Compensation** | Palantir | New York, NY | 2019-09-24T16:42:04.588000 | [Apply](https://jobs.lever.co/palantir/c6053b88-bef1-41e7-9790-8da0d8db5290) |
| **Financial Analyst - Compensation** | Palantir | Palo Alto, CA | 2019-05-31T17:56:55.655000 | [Apply](https://jobs.lever.co/palantir/41c2ee44-4131-4a7e-9ea4-8514e4950e33) |
| **Executive Team Assistant** | Palantir | Miami, FL | 2026-01-06T22:03:39.442000 | [Apply](https://jobs.lever.co/palantir/38507256-ad68-41aa-a7f6-8ab478ec6374) |
| **Deployment Strategist - US Government** | Palantir | Fayetteville, NC | 2026-01-12T22:44:40.602000 | [Apply](https://jobs.lever.co/palantir/5f39f83b-ef08-4ee8-afda-a2c77440598f) |
| **Defensive Security Analyst** | Palantir | Washington, D.C. | 2026-01-08T11:51:58.513000 | [Apply](https://jobs.lever.co/palantir/bc803bd5-7793-452d-9ae5-9301ee24615a) |
| **American Tech Fellowship for Veterans** | Palantir | North America | 2026-01-07T00:26:56.606000 | [Apply](https://jobs.lever.co/palantir/b88cd6e1-22b7-49d6-b215-1ca262a05728) |
| **Web Content Strategist** | Figma | San Francisco, CA • New York, NY • United States | 2026-01-06T13:12:19-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5736009004?gh_jid=5736009004) |
| **Strategic Program Manager, Contingent Workforce** | Figma | San Francisco, CA • New York, NY • United States | 2026-01-07T13:46:33-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5735636004?gh_jid=5735636004) |
<!-- JOBS_TABLE_END -->

## 🛠 How It Works

### The Engine
1. **Continuous Crawling**: Our scrapers monitor top job boards around the clock.
2. **Smart Classification**: We analyze job descriptions to ensure they match high-quality AI/ML criteria.
3. **Visa Check**: We look for indicators of visa sponsorship and relocation support.
4. **Instant Publishing**: New jobs are committed to this repository immediately.

### Job Categories
- 🧠 **Research Scientist**
- 💻 **AI/ML Engineer**
- 📊 **Data Scientist**
- 🗣️ **NLP Specialist**
- 👁️ **Computer Vision Engineer**

## 📝 How to Use

### Find Your Next Role
1. Navigate to the `jobs/` directory.
2. Open the latest report (e.g., `jobs/reports/jobs_report_YYYYMMDD.md`).
3. Browse jobs with clear details: **Title, Company, Salary, Location, and Apply Link**.
4. Click and apply!

### Run It Yourself (Local Development)

Want to run the scraper locally?

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-jobs.git
   cd ai-jobs
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper**
   ```bash
   python main.py
   ```

## 🚀 Technology Stack
- **Python 3.10+**
- **Playwright & Aiohttp**: For robust and fast web scraping.
- **Pandas**: For data processing and organization.
- **GitHub Actions**: For CI/CD and hourly automation.

## 📁 Project Structure
```
ai-jobs/
├── crawlers/          # Scrapers for different job boards
├── ai_filter/         # Logic to classify and filter relevant jobs
├── data/              # Data models for job entries
├── jobs/              # 📂 The Treasure Trove: Scraped job listings
├── .github/workflows/ # CI/CD configuration for hourly runs
└── main.py            # The brain of the operation
```

## 🤝 Contributing
We welcome contributions! Whether it's adding a new job source, improving the filter logic, or fixing a bug.
Check out [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## ⚖️ Ethical Scraping
- We respect `robots.txt` policies.
- We implement rate limiting to be good citizens of the web.
- All data is attributed to original sources.

## ⚠️ Disclaimer
Jobs are aggregated from public sources. While we strive for accuracy, please verify details (especially visa sponsorship) on the application page.

## 📄 License
MIT License - Free to use, modify, and distribute.

## 🙏 Acknowledgements
- Built with ❤️ for the global AI community.
- Powered by Open Source.

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

