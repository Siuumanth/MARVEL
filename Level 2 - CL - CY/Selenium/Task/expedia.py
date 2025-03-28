from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

from selenium.webdriver.chrome.options import Options

options1 = Options()
options1.add_argument("--user-data-dir=C:/Users/gsuma/AppData/Local/Google/Chrome/User Data")  # Update path
options1.add_argument("--profile-directory=Default")  # Use your default profile
options1.add_argument("--disable-gpu")

options1.add_argument("--disable-blink-features=AutomationControlled")
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("useAutomationExtension", False)


# chrome driver
driver_path = "C:/Windows/chromedriver.exe"  
service = Service(driver_path)

# Pass service to webdriver.Chrome()
driver = webdriver.Chrome(service=service, options=options1 )

# opening a website
driver.get("https://www.google.com")

# 2 seconds wait time
# we add delay because websites can detect automation if its too fast
time.sleep(3)

# scroll to make it look human
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# q is the name attribute of Google's search box.
search_box = driver.find_element(By.NAME, "q")

# Type a search query
search_box.send_keys("Selenium Python")

# Submit the search
search_box.submit()

time.sleep(5)

#driver.save_screenshot("google_search.png")

# Close the browser
driver.quit()
