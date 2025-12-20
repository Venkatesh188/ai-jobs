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
| **Platform Intelligence Engineer** | Palantir | New York, NY | 2025-12-15T21:11:27.652000 | [Apply](https://jobs.lever.co/palantir/a753a9e7-a361-426b-9c25-3cf2488c1730) |
| **Neurodivergent Fellowship** | Palantir | Washington, D.C. | 2025-12-07T23:17:15.415000 | [Apply](https://jobs.lever.co/palantir/fd952b52-7b9c-4056-a3dd-0bc41fcfe603) |
| **Neurodivergent Fellowship** | Palantir | New York, NY | 2025-12-07T22:42:55.766000 | [Apply](https://jobs.lever.co/palantir/61eaa54c-e1b7-4064-afad-f7df3d48d652) |
| **Government Contracts Specialist** | Palantir | London, United Kingdom | 2025-12-18T19:16:44.889000 | [Apply](https://jobs.lever.co/palantir/6374282c-0330-4f98-b2a8-1afc4070f8f5) |
| **Forward Deployed Software Engineer, Internship - US Government** | Palantir | Honolulu, HI | 2025-12-11T22:26:14.632000 | [Apply](https://jobs.lever.co/palantir/315f695d-04d1-4a9a-848e-cb2bec7a997e) |
| **Forward Deployed Software Engineer - UK Government** | Palantir | London, United Kingdom | 2023-01-11T17:48:32.149000 | [Apply](https://jobs.lever.co/palantir/57a3f928-e7d3-4037-8196-b38e2f867152) |
| **Forward Deployed Software Engineer** | Palantir | Stockholm, Sweden | 2021-10-19T00:03:27.848000 | [Apply](https://jobs.lever.co/palantir/d084b769-6f53-4409-afa8-c183b059b384) |
| **Forward Deployed Software Engineer** | Palantir | Warsaw, Poland | 2021-07-20T16:34:21.851000 | [Apply](https://jobs.lever.co/palantir/bf718bd3-b2ef-451e-8033-cb4d2d9c094b) |
| **Deployment Strategist, Internship - US Government** | Palantir | Honolulu, HI | 2025-12-11T22:31:15.446000 | [Apply](https://jobs.lever.co/palantir/a49d4181-a289-435a-b581-7f5af0497c8e) |
| **Deployment Strategist** | Palantir | Warsaw, Poland | 2021-10-28T04:13:08.600000 | [Apply](https://jobs.lever.co/palantir/9ace479e-a9e4-4610-a553-122d3831863a) |
| **Corporate Affairs Intern** | Palantir | New York, NY | 2025-12-10T17:45:19.438000 | [Apply](https://jobs.lever.co/palantir/ff70f5d5-7c43-4b20-9359-ff94f523d6f7) |
| **Corporate Affairs Intern** | Palantir | Washington, D.C. | 2025-12-11T19:57:21.688000 | [Apply](https://jobs.lever.co/palantir/ebbbdf79-b9d8-4d34-afb9-d741f269df10) |
| **Contract Manager** | Palantir | New York, NY | 2025-12-12T21:51:31.955000 | [Apply](https://jobs.lever.co/palantir/6e01a965-b6f9-414f-bb4b-b6b807938ba7) |
| **Strategic Program Manager** | Figma | San Francisco, CA • New York, NY • United States | 2025-12-16T16:59:08-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5737778004?gh_jid=5737778004) |
| **Solutions Consultant (Paris, France)** | Figma | Paris, France | 2025-12-16T05:00:37-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5735542004?gh_jid=5735542004) |
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

