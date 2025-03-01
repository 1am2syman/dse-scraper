# Configuration for DSE Scraper
import os

# Base Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Scraper Settings
BASE_URL = "https://www.dsebd.org/dse_close_price_archive.php"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
TIMEOUT = 30
RETRY_ATTEMPTS = 3

# Date Formats to Accept
DATE_FORMATS = [
    "%Y-%m-%d",  # YYYY-MM-DD
    "%d/%m/%Y",  # DD/MM/YYYY
    "%m/%d/%Y",  # MM/DD/YYYY
    "%Y%m%d",    # YYYYMMDD
    "%d %b %Y",  # 1 Feb 2025
    "%d %B %Y",  # 1 February 2025
    "%b %d, %Y", # Feb 1, 2025
    "%B %d, %Y", # February 1, 2025
]

# Excel Output Settings
EXCEL_SETTINGS = {
    'sheet_name': 'DSE_Close_Prices',
    'index_column': 'Date',
    'time_format': '%Y-%m-%d %H:%M:%S'
}
