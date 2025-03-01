from src.scraper import DSEScraper
from src.date_validator import DateValidator
import sys

def main():
    try:
        # Get date inputs
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Validate dates
        DateValidator.validate_date_input(start_date)
        DateValidator.validate_date_input(end_date)
        DateValidator.validate_date_order(start_date, end_date)

        # Initialize scraper
        scraper = DSEScraper()
        
        # Scrape data
        print("Scraping data...")
        data = scraper.scrape_data(start_date, end_date)
        
        # Save to Excel
        if not data.empty:
            output = scraper.save_to_excel(data, start_date, end_date)
            print(output)
        else:
            print("No data found for the specified date range")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
