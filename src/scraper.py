import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from src.date_validator import DateValidator
from config import BASE_URL, USER_AGENT, TIMEOUT, RETRY_ATTEMPTS, EXCEL_SETTINGS, DATA_DIR
import os
from tqdm import tqdm

class DSEScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': USER_AGENT})
        
    def scrape_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """Main method to scrape data between specified dates"""
        try:
            # Validate and parse dates
            start_dt = DateValidator.validate_date_input(start_date)
            end_dt = DateValidator.validate_date_input(end_date)
            DateValidator.validate_date_order(start_dt, end_dt)
            
            # Generate date range
            date_range = pd.date_range(start_dt, end_dt)
            
            # Scrape data for each date
            all_data = []
            for date in tqdm(date_range, desc="Scraping dates", unit="day"):
                data = self._scrape_single_day(date)
                if data is not None:
                    all_data.append(data)
            
            # Combine and return data
            return pd.concat(all_data, ignore_index=True)
            
        except Exception as e:
            print(f"Error during scraping: {str(e)}")
            return pd.DataFrame()

    def _scrape_single_day(self, date: datetime) -> pd.DataFrame:
        """Scrape data for a single day"""
        formatted_date = DateValidator.format_date_for_url(date)
        url = f"{BASE_URL}?startDate={formatted_date}&endDate={formatted_date}&inst=All%20Instrument&archive=data"
        
        for attempt in range(RETRY_ATTEMPTS):
            try:
                response = self.session.get(url, timeout=TIMEOUT)
                response.raise_for_status()
                return self._parse_html(response.text, date)
            except requests.RequestException as e:
                print(f"Attempt {attempt + 1} failed for {formatted_date}: {str(e)}")
                continue
        return None

    def _parse_html(self, html: str, date: datetime) -> pd.DataFrame:
        """Parse HTML content and extract data"""
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'class': 'table table-bordered background-white'})
        
        if table is None:
            return pd.DataFrame()
            
        # Extract table data
        rows = table.find_all('tr')
        headers = [th.text.strip() for th in rows[0].find_all('th')]
        data = []
        
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) == len(headers):
                data.append([col.text.strip() for col in cols])
        
        # Create DataFrame
        df = pd.DataFrame(data, columns=headers)
        df.insert(0, 'Date', date.strftime(EXCEL_SETTINGS['time_format']))
        return df

    def save_to_excel(self, df: pd.DataFrame, start_date: str, end_date: str) -> str:
        """Save scraped data to Excel file"""
        if df.empty:
            return "No data to save"
            
        # Create output directory if it doesn't exist
        os.makedirs(DATA_DIR, exist_ok=True)
        
        # Generate filename
        filename = f"DSE_Data_{start_date}_to_{end_date}.xlsx"
        filepath = os.path.join(DATA_DIR, filename)
        
        # Save to Excel
        df.to_excel(filepath, index=False, sheet_name=EXCEL_SETTINGS['sheet_name'])
        return f"Data saved to {filepath}"
