from datetime import datetime
from config import DATE_FORMATS

class DateValidator:
    @staticmethod
    def validate_date_input(date_str: str) -> datetime:
        """Validate and parse date string into datetime object"""
        # Normalize input
        date_str = date_str.strip().lower()
        
        # Try to parse numeric dates with spaces (e.g., "1 2 2025")
        parts = date_str.split()
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            try:
                day, month, year = parts
                if len(year) == 2:  # Handle 2-digit year
                    year = f"20{year}" if int(year) < 50 else f"19{year}"
                return datetime(int(year), int(month), int(day))
            except ValueError:
                pass
                
        # Try all formats
        for fmt in DATE_FORMATS:
            try:
                # Handle 2-digit year formats
                if len(date_str.split()[-1]) == 2:  # Last part is year
                    fmt = fmt.replace('%Y', '%y')
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
                
        # Try case-insensitive month parsing
        for fmt in DATE_FORMATS:
            if '%b' in fmt or '%B' in fmt:
                try:
                    # Try with first letter capitalized
                    date_str = date_str.title()
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
                    
        # Try removing commas and extra spaces
        date_str = date_str.replace(',', ' ').replace('  ', ' ').strip()
        for fmt in DATE_FORMATS:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
                
        raise ValueError(f"Date format not recognized. Accepted formats: {', '.join(DATE_FORMATS)}")

    @staticmethod
    def validate_date_order(start: datetime, end: datetime) -> bool:
        """Validate that start date is before end date"""
        if start > end:
            raise ValueError("Start date cannot be after end date")
        return True

    @staticmethod
    def format_date_for_url(date: datetime) -> str:
        """Format date for URL parameter (YYYY-MM-DD)"""
        return date.strftime("%Y-%m-%d")
