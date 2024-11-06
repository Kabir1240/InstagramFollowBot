import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


load_dotenv()
# path to chrome
USER_DATA_DIR = os.environ.get("USER_DATA_DIR")

# Instagram details
INSTAGRAM_EMAIL = os.environ.get("INSTAGRAM_EMAIL")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
# link to account
ACCOUNT_TO_FOLLOW = os.environ.get("ACCOUNT_TO_FOLLOW")

# sleep timers
LOGIN_SLEEP = 3
FIND_FOLLOWERS_SLEEP = 5
REFRESH_SLEEP = 2
FOLLOW_SLEEP = 2


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # keeps browser open even if program closes
        chrome_options.add_experimental_option("detach", True)
        # launches browser with user settings
        chrome_options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
        # launches browser in incognito
        chrome_options.add_argument("--incognito")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        
    
    def login(self):
        time.sleep(LOGIN_SLEEP)
        input_fields = self.driver.find_elements(By.TAG_NAME, "input")
        email_field = input_fields[0]
        password_field = input_fields[1]
        
        email_field.send_keys(INSTAGRAM_EMAIL)
        password_field.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)
    
    def find_followers(self):
        time.sleep(FIND_FOLLOWERS_SLEEP)
        self.driver.get(ACCOUNT_TO_FOLLOW)
        
        time.sleep(REFRESH_SLEEP)
        followers = self.driver.find_element(By.CSS_SELECTOR, "[href='/mmafighting/followers/']")
        followers.click()
    
    def follow(self):
        time.sleep(FOLLOW_SLEEP)
        
        follow_buttons = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]").find_elements(By.TAG_NAME, "button")
        
        for button in follow_buttons:
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            button.click()
            