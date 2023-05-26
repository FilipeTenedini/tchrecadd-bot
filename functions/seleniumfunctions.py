from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
load_dotenv()


EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

def make_login():
    email_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, './/*[@id="session_key"]'))
    )
    password_input = driver.find_element(By.XPATH, './/*[@id="session_password"]')
    enter_button = driver.find_element(By.XPATH, './/*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

    email_input.clear()
    email_input.send_keys(EMAIL)

    password_input.clear()
    password_input.send_keys(PASSWORD)
    
    enter_button.click()

def search_recruiter():
    search_bar_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))
    )
    search_bar_input.clear()
    search_bar_input.send_keys('Tech Recruiter')
    search_bar_input.send_keys(Keys.ENTER)
    pessoas_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button'))
    )
    pessoas_button.click()

def only_wait_element():
    only_wait = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pb2.t-black--light.t-14'))
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

def get_number_of_pages():
    MAX = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view')[-1].text
    MAX = int(MAX)
    return MAX

def get_button():
    buttons_list = driver.find_elements(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--secondary')
    return buttons_list

def make_invite(button):
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", button)
    button.click()
    time.sleep(1)
    send_invite = driver.find_element(By.CLASS_NAME, 'artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml1')
    send_invite.click()

def go_to_next_page():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    NEXT = driver.find_elements(By.CLASS_NAME, 'artdeco-button__text')[-3]
    NEXT.click()