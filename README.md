# Bright Data ChatGPT Search Scraper (Python)

[![Bright Data Promo](https://github.com/luminati-io/LinkedIn-Scraper/raw/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/)

<a href="https://githubbox.com/brightdata/bright-data-scrape-chatgpt-search-python-project?file=index.py" target="_blank">Open in CodeSandbox</a>, sign in with GitHub, then fork the repository to begin making changes.

This project provides a simple Python boilerplate for scraping [ChatGPT AI search](https://brightdata.com/products/web-scraper/chatgpt) results using the [Bright Data Web Scraper API](https://brightdata.com/products/web-scraper/chatgpt).

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output](#output)

---

## Overview

This repository demonstrates how to use the Bright Data Scraper API to trigger and download ChatGPT AI search results. It includes sample prompts and utility functions for batch and custom searches.

---

## Features

- Trigger ChatGPT AI searches via Bright Data Scraper `/trigger` API endpoint
- Monitor progress using `/progress` endpoint
- Download and save results as JSON
- Colored console output for better user experience
- Support for single, batch, and custom searches

---

## Demo

https://github.com/user-attachments/assets/5fe827aa-b672-4b57-b284-cc285ae40c2e

---

## Prerequisites

- Python 3.7 or higher
- Bright Data account with API KEY

---

## Installation

```bash
git clone https://github.com/your-org/bright-data-scrape-chatgpt-search-python-project.git
cd bright-data-scrape-chatgpt-search-python-project
pip install -r requirements.txt
```

### Dependencies

The project requires the following Python packages:
- `requests` - For making HTTP API calls
- `colorama` - For colored console output

Install them using:
```bash
pip install requests colorama
```

---

## Usage

1. **Set your Bright Data API token**
   
   Edit [`index.py`](index.py) and set your API token:
   ```python
   API_TOKEN = 'YOUR_API_TOKEN_HERE'
   ```

2. **Run the scraper**
   ```bash
   python index.py
   ```
   
   Results will be saved as a timestamped `.json` file in the project directory.

---

## Configuration

- **API Token:**  
  Get your API token from your Bright Data dashboard under Account Settings → API Key.

- **Dataset ID:**  
  The default dataset ID for ChatGPT AI Search is already set in [`index.py`](index.py):
  ```python
  DATASET_ID = 'gd_m7aof0k82r803d5bjm'
  ```

---

## Output

- Results are saved as JSON files (e.g., `chatgpt_results_2024-01-15T10-30-45.json`).
- Each file contains the raw API response from Bright Data.
- Console output provides real-time progress updates with colored formatting.

### Sample Console Output

```
🌟 ChatGPT AI Search Scraper
=============================

📋 Running sample searches...
🤖 Starting ChatGPT AI Search...
📝 Searching 3 prompts
📤 Sending JSON body:
[
  {
    "url": "https://chatgpt.com/",
    "prompt": "Top hotels in New York",
    "country": ""
  }
]
✅ Search started! Snapshot ID: abc123
⏳ Processing searches...
📊 Status: running (1/60)
📊 Status: ready (2/60)
⬇️ Downloading AI responses...
🎉 Success! Downloaded results
💾 Results saved to chatgpt_results_2024-01-15T10-30-45.json

✨ All done! Check the saved JSON file for results.
```

---
