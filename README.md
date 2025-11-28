# AI Jobs Aggregator - Engineering Case Study

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Architecture](https://img.shields.io/badge/Architecture-ETL-green)
![Status](https://img.shields.io/badge/Status-Portfolio_Project-orange)

**A distributed data pipeline for aggregating and normalizing job market data.**

> **Note for Recruiters**: This repository is a **portfolio case study** demonstrating data engineering skills (Web Scraping, ETL, Data Normalization). It is not currently operating as a live commercial service.

<<<<<<< HEAD
##  [Read the Technical Deep Dive (PORTFOLIO.md)](./PORTFOLIO.md)
=======
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
| **Software Engineer** | Udemy | Dublin, Ireland | 2025-11-28T08:00:29-05:00 | [Apply](https://app.careerpuck.com/job-board/udemy/job/5649027004?gh_jid=5649027004) |
| **Technical Support Engineer 2** | Twilio | Remote - India | 2025-11-28T03:42:40-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7431149) |
| **Phone Numbers Operations Specialist 2** | Twilio | Remote - India | 2025-11-28T04:25:36-05:00 | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7420702) |
| **Tax Analyst  (Indirect Tax)** | Okta | Bengaluru, India | 2025-11-28T08:53:01-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/7418575?gh_jid=7418575) |
| **Staff Software Engineer in Test** | Okta | Bengaluru, India | 2025-11-28T08:29:34-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/7369387?gh_jid=7369387) |
| **Senior Software Engineer, Java, Spring, Backend** | Okta | Bengaluru, India | 2025-11-28T01:31:22-05:00 | [Apply](https://www.okta.com/company/careers/opportunity/6879868?gh_jid=6879868) |
| **Customer Success Manager (Mandarin Speaking)** | Stripe | Singapore | 2025-11-28T02:38:13-05:00 | [Apply](https://stripe.com/jobs/search?gh_jid=7430701) |
| **Customer Success Manager (AUNZ)** | Stripe | Australia | 2025-11-28T01:38:40-05:00 | [Apply](https://stripe.com/jobs/search?gh_jid=7430703) |
| **Sr. Staff Software Engineer** | Pinterest | Zurich, CH | 2025-11-28T07:39:49-05:00 | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7158600) |
| **Senior AirCover Specialist** | Airbnb | Gurugram, India | 2025-11-28T07:04:47-05:00 | [Apply](https://careers.airbnb.com/positions/7427910?gh_jid=7427910) |
| **Zencastr: Senior Backend Engineer - Full Remote** | See Title/Desc | Remote | Wed, 06 Aug 2025 20:01:29 +0000 | [Apply](https://weworkremotely.com/remote-jobs/zencastr-senior-backend-engineer-full-remote) |
| **Customer Growth Lead Americas** | Immutable | nan | 2025-11-27T11:00:02+00:00 | [Apply](https://remoteOK.com/remote-jobs/remote-customer-growth-lead-americas-immutable-1129058) |
| **Graphic Designer Contract to Perm** | Monad Foundation | nan | 2025-11-27T11:00:19+00:00 | [Apply](https://remoteOK.com/remote-jobs/remote-graphic-designer-contract-to-perm-monad-foundation-1129060) |
| **Workplace Operations Analyst** | Palantir | Washington, D.C. | 2022-05-13T14:59:02.567000 | [Apply](https://jobs.lever.co/palantir/885b4e3a-fc76-4818-9b45-9386e615c74b) |
| **Web Application Developer - Defense** | Palantir | Palo Alto, CA | 2024-03-05T13:36:22.144000 | [Apply](https://jobs.lever.co/palantir/96e4295f-3af7-48e5-a2c8-74622eaf5587) |
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
>>>>>>> b5d342ad0749d61788b929ce9d20f2e08bbd724b

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

