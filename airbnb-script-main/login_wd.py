from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# TODO: need to prompt the user to input email
USER_EMAIL = "lbo@multusmanagement.com"
PASSWORD = "B3lieveSt0ne!"
MAIN_PAGE_URL = "https://www.airbnb.com/login"
LISTING_PAGE_URL = "https://www.airbnb.com/hosting/listings"
RESERVATION_URL = "https://www.airbnb.com/hosting/reservations"

XPATH_email_btn = "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/main/div/div/div/div/div/div[3]/div/div[4]/button/div/div[2]"
XPATH_login_form = "/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/main/div/div/div/div/div/form"

driver = webdriver.Chrome()
driver.get(MAIN_PAGE_URL)


def login(driver):
    # click continue with email with XPATH - doable
    email_btn = driver.find_element(By.XPATH, XPATH_email_btn)
    email_btn.click() 

    # try input user info - workable
    email_input = driver.find_element(By.NAME, "user[email]")
    email_input.send_keys(USER_EMAIL)

    # find "continue" button and click to submit email
    login_form = driver.find_element(By.XPATH, XPATH_login_form)
    login_form.submit()
    # TODO: after submitting, not shown (might need to sleep)
    time.sleep(2)

    # find password input form and input password
    pw_input = driver.find_element(By.NAME, "user[password]")
    pw_input.send_keys(PASSWORD)
    pw_input.submit()

    # TODO: SUCCESSFULLY LOGGED IN
    time.sleep(5)

# login
login(driver)



# driver.get("https://www.airbnb.com/hosting/listings")       # get listing
# get reservation
driver.get(RESERVATION_URL)

time.sleep(5)


print(driver.page_source)

# TODO: for listing
# red: <ellipse cx="8" cy="8" fill-rule="evenodd" rx="8" ry="8"></ellipse>

# gre: <ellipse cx="8" cy="8" fill-rule="evenodd" rx="8" ry="8"></ellipse>
# <svg viewBox="0 0 16 16" role="presentation" aria-hidden="true" 
# focusable="false" style="height: 10px; width: 10px; 
# fill: rgb(0, 138, 5);"><ellipse cx="8" cy="8" fill-rule="evenodd" rx="8" ry="8"></ellipse></svg>

# //*[@id="FMP-target"]/div/div/div/div[3]/div/div[4]/button
