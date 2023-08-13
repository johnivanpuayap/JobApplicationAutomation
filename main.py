import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
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

# Search for your position
search_bar = driver.find_element(By.XPATH, '//*[@id="jobs-search-box-keyword-id-ember24"]')
search_bar.send_keys(config.POSITION)
search_bar.send_keys(Keys.ENTER)

# Click the Easy Apply on the Job Posting
div_container = driver.find_element(By.XPATH,
                                    '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div['
                                    '4]/div/div/div')
easy_apply = div_container.find_element(By.TAG_NAME, 'button')
easy_apply.click()

time.sleep(100)

driver.quit()
