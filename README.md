# Automated AI Jobs Repository

## 🤖 Project Overview

This repository provides an automated, continuously updated collection of AI and research-related job postings. Powered by web scraping, AI filtering, and GitHub Actions, we eliminate manual job curation.

### 🌟 Key Features
- **Automated Hourly Scraping**: Jobs are scraped every hour from multiple sources
- **AI-Powered Filtering**: OpenAI API classifies job relevance for AI/ML positions
- **Comprehensive Job Listings**: Curated list of research and engineering positions
- **Automated Repository Updates**: GitHub Actions automatically commits new jobs

## 📊 Job Listing Stats
- **Total Jobs**: X
- **Last Updated**: [Timestamp]
- **Sources**: LinkedIn, Glassdoor, Indeed, Academic Job Boards

## 🛠 How It Works

### Scraping Process
1. **Web Crawling**: Use Crawl4AI to extract job listings from multiple sources
2. **AI Filtering**: OpenAI API classifies job relevance based on:
   - AI/ML Keywords Presence
   - Research Orientation
   - Technical Depth
   - Career Stage Alignment
3. **Data Standardization**: Normalize job information into structured format
4. **Repository Update**: Automatically commit new jobs to repository

### Job Filtering Criteria
The AI classifier filters for:
- AI/ML Research Positions
- Data Science Roles
- Machine Learning Engineering
- NLP and Computer Vision Jobs
- Academic and Industry Positions

**Excluded**: Sales, Marketing, Administrative roles

## 🔍 Job Categories
- Research Scientist
- AI Engineer
- Machine Learning Researcher
- Data Scientist
- NLP Specialist
- Computer Vision Engineer

## 📝 How to Use

### View Jobs
- Browse monthly markdown files in the `jobs/` directory
- Filter by year and month
- Click job links to apply directly

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-jobs.git
   cd ai-jobs
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

5. **Run the scraper**
   ```bash
   python main.py
   ```

## 🚀 Technology Stack
- **Web Crawling**: Crawl4AI
- **AI Filtering**: OpenAI API (GPT-4o-mini)
- **CI/CD**: GitHub Actions
- **Language**: Python 3.11+
- **Data Storage**: CSV and Markdown

## 📁 Project Structure
```
ai-jobs/
├── crawlers/          # Web crawler implementations
│   ├── base_crawler.py
│   └── linkedin_crawler.py
├── ai_filter/         # AI job classification
│   └── job_classifier.py
├── data/              # Data models and storage
│   └── job_entry.py
├── utils/             # Utility functions
│   └── logger.py
├── jobs/              # Output directory for job listings
├── logs/              # Application logs
├── config.py          # Configuration management
├── main.py            # Main entry point
└── requirements.txt   # Python dependencies
```

## 🤝 Contributing
Interested in contributing? Check out our [CONTRIBUTING.md](CONTRIBUTING.md)

### Contribution Areas
- Add new job sources (Glassdoor, Indeed, etc.)
- Improve AI filtering accuracy
- Enhance data extraction
- Optimize scraping performance

## ⚖️ Ethical Considerations
- **Respects robots.txt**: All crawlers respect website robots.txt files
- **Rate Limiting**: Implements delays between requests
- **Source Attribution**: All jobs include source attribution
- **Terms of Service**: Compliant with website terms of service

## ⚠️ Disclaimer
- Jobs are scraped from public sources
- No guarantee of job availability
- Always verify job details with the original source
- This tool is for informational purposes only

## 📄 License
MIT License - Free to use, modify, and distribute

## 🙏 Acknowledgements
- Inspired by [2026-AI-College-Jobs](https://github.com/speedyapply/2026-AI-College-Jobs)
- Community-driven open-source project

---

**Help us improve!** ⭐ Star the repo, file issues, or contribute!

