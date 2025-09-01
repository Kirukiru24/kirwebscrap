Web Scraper with Streamlit UI

A Python-based web scraping tool with a Streamlit user interface that allows users to input a webpage URL and scrape all paragraph texts from that page. The scraped text can be viewed in the UI and saved as a local file.

This project supports scraping news articles in local languages, such as Afaan Oromo or Tigrinya, and can be extended to other websites.

Features

User-friendly Streamlit UI for URL input.

Scrapes all <p> paragraph texts from the specified URL.

Displays sample paragraphs in the UI.

Saves the full scraped text to a local .txt file.

Compatible with Python 3.x.

Ignores installed packages when pushing to GitHub using .gitignore.

Demo Screenshot

(Add a screenshot of the Streamlit app if you like)

Installation

Clone the repository

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name


Create a virtual environment

python -m venv venv


Activate the virtual environment

Windows (Command Prompt):

venv\Scripts\activate


PowerShell:

.\venv\Scripts\Activate.ps1


Linux / MacOS:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt

Usage

Run the Streamlit app:

streamlit run app.py


Open the URL shown in the terminal (usually http://localhost:8501).

Enter the webpage URL you want to scrape in the text box.

Click "Scrape Text" to fetch paragraphs.

View sample paragraphs in the app and save the full text to a local file.

File Structure
webscrapping/
├─ app.py                 # Streamlit UI + scraping logic
├─ scrape.py              # Optional standalone scraping script
├─ requirements.txt       # Python dependencies
├─ .gitignore             # Excludes venv, cache, VS Code files
└─ venv/                  # Python virtual environment (ignored by Git)

Dependencies

streamlit

requests

beautifulsoup4

All dependencies are listed in requirements.txt.

How to Contribute

Fork the repository.

Create a new branch: git checkout -b feature/your-feature

Make changes and commit: git commit -m "Add your feature"

Push to branch: git push origin feature/your-feature

Open a pull request.

License

This project is open-source and available under the MIT License.
