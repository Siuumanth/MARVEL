from bs4 import BeautifulSoup

# Open and read the local HTML file
with open("D:\code\marvel\Level 2 - CL - CY\Selenium\practical\page.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")



# Find all divs with an aria-label attribute
divs_with_aria = soup.find_all("li", attrs={"aria-label": True})

# Extract and print the aria-label values
for div in divs_with_aria:
    print(div["aria-label"])
