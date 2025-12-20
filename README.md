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
| **Field Enablement Manager (London, United Kingdom)** | Figma | London, England | 2025-12-19T16:13:40-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5741316004?gh_jid=5741316004) |
| **Director, Digital Customer Success** | Udemy | San Francisco, CA | 2025-12-19T16:31:42-05:00 | [Apply](https://app.careerpuck.com/job-board/udemy/job/5733307004?gh_jid=5733307004) |
| **Director, Digital Customer Success** | Udemy | Austin, TX | 2025-12-19T16:34:30-05:00 | [Apply](https://app.careerpuck.com/job-board/udemy/job/5741851004?gh_jid=5741851004) |
| ** Director, Digital Customer Success** | Udemy | Denver, CO | 2025-12-19T16:34:02-05:00 | [Apply](https://app.careerpuck.com/job-board/udemy/job/5741849004?gh_jid=5741849004) |
| **Senior Investigator ** | Twilio | Remote - US | 2025-12-19T17:03:11-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7466463) |
| **Art Director** | Twilio | Remote - US | 2025-12-19T17:03:11-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7474214) |
| **Full Stack Software Engineer, Credit Cards and Banking** | Robinhood | Menlo Park, CA; New York, NY | 2025-12-19T17:13:13-05:00 | [Apply](https://boards.greenhouse.io/robinhood/jobs/7170008?t=gh_src=&gh_jid=7170008) |
| **Finance & Strategy Manager** | Robinhood | Chicago, IL; Menlo Park, CA; New York, NY | 2025-12-19T16:40:27-05:00 | [Apply](https://boards.greenhouse.io/robinhood/jobs/7473331?t=gh_src=&gh_jid=7473331) |
| **Senior Software Engineer, Android Test Engineering** | Reddit | Los Angeles, CA | 2025-12-19T17:06:43-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7488988) |
| **Senior Software Engineer, Android Test Engineering** | Reddit | Remote - United States | 2025-12-19T17:05:57-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7488862) |
| **Senior Software Engineer, Android Test Engineering** | Reddit | Chicago, IL | 2025-12-19T17:06:45-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7488991) |
| **Senior Software Engineer, Android Test Engineering** | Reddit | New York City, NY | 2025-12-19T17:06:46-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7488992) |
| **Senior Software Engineer, Android Test Engineering** | Reddit | San Francisco, CA | 2025-12-19T17:06:42-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7488986) |
| **Engineering Manager - Ads Data Platform** | Reddit | Remote - Ontario, Canada | 2025-12-19T17:25:13-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7489117) |
| **Peloton Expert** | Peloton | United Kingdom | 2025-12-19T15:11:26-05:00 | [Apply](https://careers.onepeloton.com/en/all-jobs/?gh_jid=7482216) |
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

