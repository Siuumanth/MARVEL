from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

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

# Parse the page using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the relevant flight details
flights = soup.find_all('div', {'class': 'VswJJe'})  # This class may change based on Google Flights' structure

# Extract flight details and store them in a dictionary
flight_details = []
for flight in flights:
    try:
        # Extracting flight information, adjust according to actual element classes and structure
        departure_time = flight.find('div', {'class': 'VdS7Gc'}).text.strip() if flight.find('div', {'class': 'VdS7Gc'}) else None
        arrival_time = flight.find('div', {'class': 'Nau7mf'}).text.strip() if flight.find('div', {'class': 'Nau7mf'}) else None
        airline = flight.find('div', {'class': 'ktXwX'}).text.strip() if flight.find('div', {'class': 'ktXwX'}) else None
        price = flight.find('div', {'class': 'YMlIz'}).text.strip() if flight.find('div', {'class': 'YMlIz'}) else None
        
        flight_details.append({
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'airline': airline,
            'price': price
        })
    except Exception as e:
        print(f"Error extracting flight details: {e}")

# Print the scraped details
if flight_details:
    print("\nFlight Details:")
    for flight in flight_details:
        print(flight)
else:
    print("No flights found.")

# Close the browser
time.sleep(10)  # Shorter delay before closing
driver.quit()
print("Browser closed")
