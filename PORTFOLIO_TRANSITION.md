# Portfolio Transition Plan

This document outlines the steps to convert the "AI Jobs" project from a live scraper into a professional engineering portfolio case study.

## 1. Validation of Strategy
The approach to pivot to a "Portfolio Case Study" is **correct and recommended**.
- **Legal Safety**: Removes risks associated with ToS violations and IP bans.
- **Maintenance**: Eliminates the need for constant fixes when target sites change.
- **Value**: Shifts focus from "I can run a script" to "I can architect a data pipeline".

## 2. Action Plan

### Phase 1: Repository Cleanup & Safety
- [ ] **Update `.gitignore`**: Ensure raw data (CSVs, logs) are not committed.
- [ ] **Sanitize Code**: Ensure no API keys or sensitive headers are hardcoded.
- [ ] **License & Disclaimer**: Add strict educational use disclaimers.

### Phase 2: Rebranding (The "Case Study" Look)
- [ ] **Rewrite `README.md`**: 
    - Remove "Hourly Updates" promises.
    - Add "Architecture Diagram" (text/mermaid).
    - Highlight "Engineering Challenges" (Normalization, Rate Limiting).
- [ ] **Create `PORTFOLIO.md`**: A deep dive into the technical implementation for recruiters.

### Phase 3: The Static Demo
- [ ] **Generate Static Dataset**: Create a script to produce a clean `jobs_sample.json` from your local scrapes.
- [ ] **Build Frontend**: Create a simple HTML/JS dashboard in a `docs/` folder.
    - Why `docs/`? GitHub Pages can serve directly from this folder on the main branch.
- [ ] **Host**: Enable GitHub Pages on the `docs/` folder.

## 3. Resume "Flex" (Copy-Paste)

**Project: Distributed Job Data Aggregation Pipeline**
*Designed and implemented a scalable ETL pipeline to aggregate job market data for analysis.*
- **Architecture**: Built a modular Python scraper with `BeautifulSoup` and `Selenium`, utilizing Strategy Pattern for extensible crawler additions.
- **Data Engineering**: Developed normalization pipelines to unify disparate JSON/HTML schemas from 4+ sources into a standardized format.
- **Resilience**: Implemented intelligent rate-limiting, user-agent rotation, and exponential backoff to mimic human behavior and respect server load.
- **Frontend**: Deployed a static React/JS dashboard to visualize aggregated data, hosted on GitHub Pages.
- **Tech Stack**: Python, Pandas, GitHub Actions, JavaScript.

## 4. Next Steps for You
1. Run the `generate_static_site.py` script (we will create this).
2. Go to Repo Settings -> Pages -> Source: `main` branch, `docs` folder.
3. Add the link to your resume.
