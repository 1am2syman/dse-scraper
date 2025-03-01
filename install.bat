@echo off
echo Cloning repository...
git clone https://github.com/yourusername/dse-scraper.git || exit /b
cd dse-scraper
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
echo Installation complete! Run 'python main.py' to start
