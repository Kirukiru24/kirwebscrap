Web Scraper with Streamlit UI






A simple Python web scraper with Streamlit UI that allows users to input any webpage URL and scrape all paragraph texts. Works well for local languages like Afaan Oromo or Tigrinya.

Features

User-friendly Streamlit interface for URL input.

Scrapes all <p> paragraph texts from a webpage.

Displays sample paragraphs in the app.

Saves full scraped text to a .txt file.

Lightweight and easy to run.

Quick Start

Clone repository

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


Create and activate virtual environment

python -m venv venv
# Windows (cmd):
venv\Scripts\activate
# PowerShell:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the Streamlit app

streamlit run app.py


Enter a URL in the app and click "Scrape Text".

File Structure
webscrapping/
├─ app.py             # Streamlit UI + scraper
├─ requirements.txt   # Dependencies
├─ .gitignore         # Ignores venv, cache, VS Code files
└─ venv/              # Python virtual environment (ignored)

License

MIT License – free to use and modify.
