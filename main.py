import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import config

# Using Selenium with a webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url=config.SIGN_IN_URL)

# Sign In
email_input = driver.find_element(By.NAME, 'session_key')
email_input.send_keys(config.EMAIL)
password_input = driver.find_element(By.NAME, 'session_password')
password_input.send_keys(config.PASSWORD)
password_input.send_keys(Keys.ENTER)

# Go to the Job Posting
driver.get(url=config.JOB_SEARCH_URL)


time.sleep(100)

driver.quit()
