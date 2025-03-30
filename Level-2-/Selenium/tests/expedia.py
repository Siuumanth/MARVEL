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
options1.add_argument("--user-data-dir=C:/Users/gsuma/AppData/Local/Google/Chrome/User Data")  
options1.add_argument("--profile-directory=Default")  
options1.add_argument("--disable-gpu")
options1.add_argument("--disable-blink-features=AutomationControlled")
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("useAutomationExtension", False)

# Set Chrome Driver path
driver_path = "C:/Windows/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options1)

# Open Expedia
driver.get("https://www.expedia.com/Flights")
print("Opened Expedia flight page")

# Wait for page load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Select "From" field and enter departure city
from_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Leaving from')]")))
from_input.click()
time.sleep(1)

# Close the dialog box if it appears
try:
    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Close')]"))
    )
    close_button.click()
    print("Closed the 'Leaving from' dialog box")
except:
    print("No dialog box appeared for 'Leaving from'")

# Interact with the input field after closing the dialog box (or if no dialog)
from_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='location-field-leg1-origin']")))
from_field.clear()
from_field.send_keys("New York")
time.sleep(1)  
from_field.send_keys("\n")
print("Entered departure city")

# Select "To" field and enter destination city
to_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Going to')]")))
to_input.click()
time.sleep(1)

# Close the dialog box if it appears
try:
    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Close')]"))
    )
    close_button.click()
    print("Closed the 'Going to' dialog box")
except:
    print("No dialog box appeared for 'Going to'")

# Interact with the input field after closing the dialog box (or if no dialog)
to_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='location-field-leg1-destination']")))
to_field.clear()
to_field.send_keys("London")
time.sleep(1)  
to_field.send_keys("\n")
print("Entered destination city")

# Click the search button
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'search-button')]")))
search_button.click()
print("Clicked search button")

# Wait for flight results to load
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'results-list')]")))
print("Flight results loaded")

# Parse page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
flights = soup.find_all('li', {'class': 'uitk-spacing'})

# Extract flight details
if flights:
    print("\nFlight Results Found:")
    for flight in flights[:5]:  # Limit to first 5 results
        print(flight.text.strip())
else:
    print("No flights found, Expedia might be blocking the request.")

# Close the browser
time.sleep(15)  # Shorter delay before closing
driver.quit()
print("Browser closed")
