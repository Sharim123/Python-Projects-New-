from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    service = Service("C:/Users/shari/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    # Extract only the temp
    output = int(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    username = driver.find_element(By.ID, "id_username")
    password = driver.find_element(By.ID, "id_password")
    username.send_keys("automated")
    time.sleep(2)
    password.send_keys("automatedautomated" + Keys.ENTER)
    driver.find_element(By.XPATH, '/html/body/nav/div/a').click()
    temp = driver.find_element(By.XPATH, '//*[@id="displaytimer"]')
    time.sleep(2)
    return clean_text(text=temp.text)

print(main())















