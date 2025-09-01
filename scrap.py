import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlit UI
st.title("Web Scraper for Text Extraction")
st.write("Enter a webpage URL to scrape all paragraph texts:")

# Input box for URL
url = st.text_input("Enter the full URL", "https://www.bbc.com/tigrinya/articles/c07p42jz88lo")

if st.button("Scrape Text"):
    if not url.startswith("http"):
        st.error("Please enter a valid URL starting with http or https")
    else:
        try:
            # Fetch page
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                
                # Extract paragraphs
                paragraphs = soup.find_all("p")
                scraped_text = [p.get_text() for p in paragraphs]

                if scraped_text:
                    st.success(f"Scraped {len(scraped_text)} paragraphs!")
                    
                    # Display first 10 paragraphs
                    st.subheader("Sample Paragraphs:")
                    for para in scraped_text[:10]:
                        st.write(para)

                    # Save to file
                    filename = "scraped_text.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        for line in scraped_text:
                            f.write(line + "\n")
                    st.success(f"Full text saved to {filename}")
                else:
                    st.warning("No paragraphs found on this page.")
            else:
                st.error(f"Failed to fetch the page. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
