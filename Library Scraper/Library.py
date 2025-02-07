from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Database setup
db_name = "libraries.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS libraries (
    state TEXT,
    city TEXT,
    library TEXT,
    address TEXT,
    zip TEXT,
    phone TEXT
)
''')
conn.commit()

# Selenium WebDriver setup
driver_path = r"C:\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

driver = webdriver.Chrome(service=service, options=options)

# Base URL
base_url = "https://publiclibraries.com/state/"
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "District of Columbia", "Florida"
]

# Scraping function
def scrape_state_libraries(state):
    logging.info(f"Scraping libraries for {state}...")
    state_url = f"{base_url}{state.lower().replace(' ', '-')}"
    driver.get(state_url)

    try:
        # Wait for the table to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip header row

        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 5:
                city = cols[0].text.strip()
                library = cols[1].text.strip()
                address = cols[2].text.strip()
                zip_code = cols[3].text.strip()
                phone = cols[4].text.strip()

                # Save data to SQLite
                cursor.execute('''
                    INSERT INTO libraries (state, city, library, address, zip, phone)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (state, city, library, address, zip_code, phone))
        conn.commit()
    except Exception as e:
        logging.error(f"Error scraping {state}: {e}")

# Scrape all states
for state in states:
    scrape_state_libraries(state)

# Close resources
driver.quit()
conn.close()

logging.info("Scraping completed. Data saved to libraries.db.")
