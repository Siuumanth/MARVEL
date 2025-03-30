from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

# Get the page source (HTML)
html_content = driver.page_source
print(html_content)

# Close the browser
driver.quit()
