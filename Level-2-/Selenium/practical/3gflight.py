from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pandas as pd  


from_dest = "Bengaluru"
to_dest = "New Delhi"

from_date = "29/03/2025"
return_date = "30/03/2025"


# chrome options
options = Options()
options.add_argument("--user-data-dir=C:/Users/gsuma/AppData/Local/Google/Chrome/User Data")  
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver_path = "C:/Windows/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# opening google flights
driver.get("https://www.google.com/travel/flights")
time.sleep(1)
print("Opened Google Flights page")






time.sleep(2)

# London in Where to? box
active_element = driver.switch_to.active_element
active_element.send_keys(to_dest)
time.sleep(1)

# pressing tab twice to move to next box
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).pause(0.5).send_keys(Keys.TAB).perform()
print("went to dep date field")

time.sleep(1)

# departure date
departure_date = from_date
active_element = driver.switch_to.active_element
active_element.send_keys(departure_date)
print(f"entered dep Date: {departure_date}")

time.sleep(1)

#  TAB to move to return date
actions.send_keys(Keys.TAB).perform()
print("Moved to Return date field")

time.sleep(1)

# entering return date
return_date = return_date
active_element = driver.switch_to.active_element
active_element.send_keys(return_date)
print(f"Entered Return Date: {return_date}")

time.sleep(1)

# ENTER to confirm
active_element.send_keys(Keys.ENTER)
# TAB twice to move to the next field
actions.send_keys(Keys.TAB).pause(0.5).send_keys(Keys.TAB).perform()
print("Moved to the next field")

time.sleep(1)

# ENTER on the active element
active_element = driver.switch_to.active_element
active_element.send_keys(Keys.ENTER)
print("Confirmed selection with ENTER")

print("Search initiated!")




# Going to next page ::

# ensure elements have loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# scrolling multiple times to load everything
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # allowing time for content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# wating for divs with aria-label to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label]')))

# extracting aria-labels of divs that start with "From"
divs = driver.find_elements(By.XPATH, '//div[@aria-label]')
filtered_labels = [div.get_attribute("aria-label") for div in divs if div.get_attribute("aria-label") and div.get_attribute("aria-label").startswith("From")]

print(filtered_labels)



# saving extracted flight data to a txt file
with open("flight_data.txt", "w", encoding="utf-8") as file:
    for label in filtered_labels:
        file.write(label + "\n")

print("Flight data saved to flight_data.txt")




time.sleep(0) 
driver.quit()
print("Browser closed")

