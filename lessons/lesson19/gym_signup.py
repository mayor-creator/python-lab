import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(5)

driver.get("https://appbrewery.github.io/gym/")

# locate the login button and click on it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(0.5)

# locate the form up and send login credentials
signup_form = driver.find_element(By.ID, "login-form")
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

# enter credentials into the forms
email_input.send_keys("student@test.com")
password_input.send_keys("password123")

# submit the form to login
signup_form.submit()

# find an exercise class and click on book
book_exercise_button = driver.find_element(By.ID, "book-button-hiit-2026-09-02-0900")
book_exercise_button.click()

# keep the window open until quit
input("Press Enter in the terminal to close the browser and quit...")
driver.quit()
