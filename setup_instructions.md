# Setup Instructions

## Prerequisites
- Python 3.11 or higher
- OpenAI API key
- Git (for version control)

## Step-by-Step Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-jobs.git
cd ai-jobs
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Test the Setup
Run a test scrape:
```bash
python main.py
```

## GitHub Actions Setup

### 1. Add Secrets to GitHub
1. Go to your repository settings
2. Navigate to "Secrets and variables" > "Actions"
3. Add a new secret:
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key

### 2. Enable GitHub Actions
The workflow will automatically run:
- Every hour (scheduled)
- On every push to main branch
- Manually via workflow_dispatch

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again

2. **OpenAI API Errors**
   - Verify your API key is correct
   - Check your OpenAI account has credits
   - Ensure API key has proper permissions

3. **Crawling Errors**
   - LinkedIn may block automated requests
   - Check internet connection
   - Verify robots.txt is accessible

4. **Permission Errors**
   - Ensure write permissions for `jobs/` and `logs/` directories
   - Check file permissions on Windows/Mac/Linux

## Development Mode

For development, you can modify the scraper settings in `config.py` or via environment variables.

### Example: Local Testing
```python
# Reduce max_pages for faster testing
search_params = {
    "keywords": "AI Machine Learning",
    "max_pages": 1  # Only crawl 1 page
}
```

