from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options
options = Options()
options.add_argument("--user-data-dir=C:/Users/gsuma/AppData/Local/Google/Chrome/User Data")  # Update path
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Set Chrome Driver path
driver_path = "C:/Windows/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open Google Flights
driver.get("https://www.google.com/travel/flights")
time.sleep(5)
print("Opened Google Flights page")

# Click "From" field
from_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']"))
)
from_field.click()
time.sleep(1)
from_field.send_keys("New York")
time.sleep(2)
from_field.send_keys("\n")
print("Entered departure city")

# Click "To" field
to_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']"))
)
to_field.click()
time.sleep(1)
to_field.send_keys("London")
time.sleep(2)
to_field.send_keys("\n")
print("Entered destination city")

# Click the search button (Google Flights updates results automatically)
time.sleep(5)
print("Searching for flights...")



# Ensure the "From" field is clickable
from_field = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']"))
)

# Use JavaScript to set the value
driver.execute_script("arguments[0].value = 'New York';", from_field)
print("Entered departure city")

# Ensure the "To" field is clickable
to_field = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']"))
)

# Use JavaScript to set the value
driver.execute_script("arguments[0].value = 'London';", to_field)
print("Entered destination city")

# Wait a bit to let Google Flights automatically update the results
time.sleep(5)
print("Searching for flights...")






# Wait for results to load
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='pIav2d']"))
)
print("Flight results loaded")

# Close the browser
time.sleep(20)
driver.quit()
print("Browser closed")
