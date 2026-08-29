from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(5)

# navigate to the website url
driver.get("https://bandcamp.com/discover")
print(driver.title)

# locate an element using id selector
pagination_button = driver.find_element(By.ID, "view-more")
print(pagination_button.accessible_name)

# locate an element using class selector
tracks = driver.find_elements(By.CLASS_NAME, "results-grid-item")
print(len(tracks))
print(tracks[0].text)

# interact with button element
# button = driver.find_element(By.ID, "submit-button")
# button.click()

# send keystrokes and text entry
search_box = driver.find_element(By.TAG_NAME, "input")
search_box.send_keys("Search for this")
# search_box.submit()
search_box.send_keys(Keys.ENTER)

driver.quit()
