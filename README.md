### Browser Investigator

## Overview

Browser Investigator is a Python-based digital forensics tool designed to extract and analyze browser history from Chromium-based browsers. It helps investigators, students, and cybersecurity enthusiasts explore browsing activity by generating meaningful insights such as browsing timelines, active hours, most visited domains, top pages, keyword-based searches, and statistical summaries.

The project follows a modular architecture, separating data extraction from data analysis, making it easy to extend with additional forensic artifacts such as downloads, bookmarks, cookies, and saved passwords in future versions.

## Features 

- Extract browser history from thr Chromium-based browsers
- Analyze browsing timelines
- Identify most acive browsing hours
- Discover top visited domains 
- Rank most visited web pages 
- Search browsing history using keywords 
- Generate browsing statistics
- Modular architecture for future forensic extensions

## Project Structure

browser-investigator/
│
├── extractors/
│   └── chrome_extractor.py    # Extract browser history
│
├── analyzer.py                # Browser history analysis engine
├── main.py                    # Entry point
├── requirements.txt           # Project dependencies
└── README.md

## Tech stack

- Python3
- SQLite
- Pandas 
- urlib.parse

## Current Status 

### Completed 

- [X] Browser History Extraction
- [X] Timeline Analysis
- [X] Active Hours Analysis
- [X] Top Domains
- [X] Top Pages
- [X] Keyword Search
- [X] Statistics Dashboard

### Planned 

- [ ] Downloads Extraction
- [ ] Bookmarks Extraction
- [ ] Cookies Metadata
- [ ] Search Terms Extraction
- [ ] CSV Export
- [ ] Flask Dashboard
- [ ] Firefox Support
- [ ] Edge Support

