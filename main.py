from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from functions.seleniumfunctions import make_login, search_recruiter, only_wait_element, get_number_of_pages, driver, get_button, make_invite, go_to_next_page, press_esc

make_login()
search_recruiter()
only_wait_element()
MAX = get_number_of_pages()

for i in range(0, MAX, 1):
    only_wait = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pb2.t-black--light.t-14'))
    )
    time.sleep(2)
    buttons_list = get_button()

    for i, button in enumerate(buttons_list):
        try:
            if 'Conectar' in button.text and i != 0:
                make_invite(button)
        except:
            continue
    press_esc()
    go_to_next_page()
