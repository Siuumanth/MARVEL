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
time.sleep(1)
print("Opened Google Flights page")

'''
# Click "From" field
from_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']"))
)
from_field.click()
time.sleep(1)
from_field.clear() 
from_field.send_keys("Bealuru")
time.sleep(2)
from_field.send_keys("")
print("Entered departure city")


# Click a random spot on the page to close the dropdown
actions = ActionChains(driver)
random_x = random.randint(100, 500)  # Adjust range based on your screen
random_y = random.randint(100, 500)
actions.move_by_offset(random_x, random_y).click().perform()
time.sleep(1)  # Allow time for the click effect

print("Clicked a random spot to close the dropdown")

# Click "To" field
to_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']"))
)
to_field.click()
time.sleep(1)
from_field.clear() 
to_field.send_keys("London")
time.sleep(2)
to_field.send_keys("")
print("Entered destination city")
# Click "To" field
to_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']"))
)
to_field.click()
time.sleep(1)

# Use JavaScript to disable autocomplete and aria attributes
driver.execute_script("""
    arguments[0].removeAttribute('aria-autocomplete');
    arguments[0].removeAttribute('autocomplete');
    arguments[0].removeAttribute('aria-haspopup');
""", to_field)

# Use JavaScript to clear the field and set the value
driver.execute_script("arguments[0].value = '';", to_field)  # Clear field
driver.execute_script("arguments[0].value = 'London';", to_field)  # Set value
time.sleep(1)

# Trigger an input event to simulate user typing
driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", to_field)

# Send ENTER to confirm
to_field.send_keys("\n")
time.sleep(2)
'''


# Ensure page loads fully
time.sleep(2)

# Send "London" directly to the currently focused field (which should be "Where to?")
active_element = driver.switch_to.active_element
active_element.send_keys("London")
time.sleep(1)

# Press ENTER to confirm
active_element.send_keys(Keys.ENTER)
#active_element.send_keys("\n")
print("Entered destination city")

# Click the search button (Google Flights updates results automatically)
print("Entered destination city")



from_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']"))
)

from_field.click()
time.sleep(1)
from_field.clear() 
from_field.send_keys("Bealuru")
time.sleep(2)
from_field.send_keys("\n")
print("Entered departure city")

from_field.send_keys("\n")
# Click the search button (Google Flights updates results automatically)
time.sleep(5)
print("Searching for flights...")



print("Flight results loaded")






# Close the browser
time.sleep(40)  # Shorter delay before closing
driver.quit()
print("Browser closed")
