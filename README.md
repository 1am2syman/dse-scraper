# DSE Scraper

A Python tool for scraping historical stock data from the Dhaka Stock Exchange (DSE) website.

## Features
- Scrape historical stock data between specified dates
- Support for multiple date formats
- Automatic date validation
- Save data to Excel format
- Built-in error handling and retry mechanism
- Progress bar visualization

## Installation (GitHub Users)

1. Clone repository:
```bash
git clone https://github.com/1am2syman/dse-scraper.git
cd dse-scraper
```

2. Setup environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. First run:
```bash
python main.py
```

## Alternative Setup for New Users
If you don't have Python installed:
1. Download installer from [python.org](https://www.python.org/downloads/)
2. Check "Add Python to PATH" during installation
3. Proceed with steps above

## Usage

Run the scraper:
```bash
python main.py
```

Follow the prompts to enter start and end dates.

## Supported Date Formats
- YYYY-MM-DD
- DD/MM/YYYY
- MM/DD/YYYY
- YYYYMMDD
- 1 Feb 2025
- 1 February 2025
- Feb 1, 2025
- February 1, 2025

## Output
Data is saved in Excel format in the `data/` directory with filename pattern:
`DSE_Data_<start_date>_to_<end_date>.xlsx`

## Requirements
- Python 3.11+
- See requirements.txt for dependencies
