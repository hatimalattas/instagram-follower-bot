import os
import time
from selenium import webdriver

CHROME_DRIVER_PATH = "/Users/hatimalattas/Development/chromedriver"
SIMILAR_ACCOUNT = "meme_coding"
INSTAGRAM_USERNAME = os.environ.get("USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_field = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
        username_field.send_keys(INSTAGRAM_USERNAME)
        password_field = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
        password_field.send_keys(INSTAGRAM_PASSWORD)
        login_btn = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button')
        login_btn.click()

    def find_followers(self):
        time.sleep(3)
        notifications_prompt = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notifications_prompt.click()
        search_field = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]')
        search_field.click()
        search_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_input.send_keys(SIMILAR_ACCOUNT)
        time.sleep(3)
        select_account = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
        select_account.click()

    def follow(self):
        time.sleep(3)
        # to open followers list
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)

        while True:
            followers_list = self.driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')

            for f in followers_list:
                f.find_element_by_class_name("y3zKF").click()

            scr = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr)


instagram_bot = InstaFollower()
instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
