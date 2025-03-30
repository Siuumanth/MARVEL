from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set Chrome options
options1 = Options()
options1.add_argument("--user-data-dir=C:/Users/gsuma/AppData/Local/Google/Chrome/User Data")  # Update path
options1.add_argument("--profile-directory=Default")  # Use your default profile
options1.add_argument("--disable-gpu")
options1.add_argument("--disable-blink-features=AutomationControlled")
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("useAutomationExtension", False)

# Set Chrome Driver path
driver_path = "C:/Windows/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options1)

print("[LOG] Opening Skyscanner...")
driver.get("https://www.skyscanner.net")

# Wait for page to load
time.sleep(5)
print("[LOG] Page loaded successfully.")

# Scroll to make sure elements are visible
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2.5)
print("[LOG] Scrolled down for better visibility.")

# 1️⃣ Select "From" field and enter departure city
print("[LOG] Selecting 'From' field...")
from_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fsc-origin-search']")))
from_input.clear()
from_input.send_keys("New York")
print("[LOG] Entered departure city: New York")

time.sleep(1)  # Wait for suggestions to load
from_input.send_keys("\n")  # Press Enter to select the first suggestion

# 2️⃣ Select "To" field and enter destination city
print("[LOG] Selecting 'To' field...")
to_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='fsc-destination-search']")))
to_input.clear()
to_input.send_keys("London")
print("[LOG] Entered destination city: London")

time.sleep(1)  # Wait for suggestions to load
to_input.send_keys("\n")  # Press Enter to select the first suggestion

# 3️⃣ Click the search button
print("[LOG] Clicking search button...")
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'BpkButton_bpk-button')]")))
search_button.click()

# 4️⃣ Wait for flight results to load
print("[LOG] Waiting for flight results...")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "day-list-item")))
print("[LOG] Flight results loaded.")

# Parse page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 5️⃣ Extract flight details
print("[LOG] Extracting flight details...")
flights = soup.find_all('div', {'class': 'flight-details'})

if flights:
    print("[LOG] Flight Results Found:")
    for flight in flights:
        print(flight.text.strip())
else:
    print("[LOG] No flights found, Skyscanner might be blocking the request.")

# Wait a few seconds before closing
time.sleep(20)
print("[LOG] Closing the browser...")

driver.quit()
print("[LOG] Script execution finished.")
