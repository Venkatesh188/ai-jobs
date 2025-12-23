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
| **Manager, Product Support - Figma Weave (London, United Kingdom or Tel Aviv, Israel) ** | Figma | Tel Aviv, Israel • London, England | 2025-12-22T11:17:47-05:00 | [Apply](https://boards.greenhouse.io/figma/jobs/5741609004?gh_jid=5741609004) |
| **Customer Success Specialist, Pooled** | Udemy | Denver, CO | 2025-12-22T15:58:39-05:00 | [Apply](https://app.careerpuck.com/job-board/udemy/job/5740033004?gh_jid=5740033004) |
| **Technical Support Engineer - Italian Speaking ** | Twilio | Remote - Ireland | 2025-12-22T10:30:50-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7362421) |
| **Senior Account Executive** | Twilio | Remote - Singapore | 2025-12-22T01:57:42-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7479361) |
| **Compliance Operations Specialist P1** | Twilio | Remote - India | 2025-12-22T10:29:42-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7365257) |
| **Compliance Operations Specialist 1** | Twilio | Remote - India | 2025-12-22T10:28:32-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7349785) |
| **Director and Associate General Counsel, Regulatory** | Robinhood | Menlo Park, CA; New York, NY; Washington, DC | 2025-12-22T14:59:12-05:00 | [Apply](https://boards.greenhouse.io/robinhood/jobs/7354048?t=gh_src=&gh_jid=7354048) |
| **Manager, Program Management (Vendor Operations)** | Reddit | Remote - United States | 2025-12-22T14:11:23-05:00 | [Apply](https://job-boards.greenhouse.io/reddit/jobs/7492101) |
| **Senior Stock Plan Administrator** | Peloton | United States | 2025-12-22T09:24:38-05:00 | [Apply](https://careers.onepeloton.com/en/all-jobs/?gh_jid=7471881) |
| **Legal Director, Product Safety** | Peloton | Woodinville, Washington | 2025-12-22T13:02:19-05:00 | [Apply](https://careers.onepeloton.com/en/all-jobs/?gh_jid=7491937) |
| **Software Engineer I - Product Development ** | PagerDuty | San Francisco | 2025-12-22T15:50:44-05:00 | [Apply](https://job-boards.greenhouse.io/pagerduty/jobs/5722204004) |
| **Strategic Account Executive, Auth0** | Okta | Sydney, Australia | 2025-12-22T16:04:25-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/7456897?gh_jid=7456897) |
| **Solutions Engineer, Okta** | Okta | Georgia; New York, New York; North Carolina; Washington, DC | 2025-12-22T14:07:45-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/7487711?gh_jid=7487711) |
| **Associate Software Engineer in Test** | Okta | Chicago, Illinois; New York, New York; Washington, DC | 2025-12-22T12:58:50-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/7491928?gh_jid=7491928) |
| **Staff Product Manager, Software Supply Chain Security** | GitLab | Remote | 2025-12-22T13:47:13-05:00 | [Apply](https://job-boards.greenhouse.io/gitlab/jobs/8332463002) |
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

