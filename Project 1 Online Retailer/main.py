from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver():
    service = Service("C:/Users/shari/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver

def process():
    driver = get_driver()

    email = driver.find_element(By.ID, "CustomerEmail")
    password = driver.find_element(By.ID, "CustomerPassword")

    email.send_keys("sharimrauf@gmail.com")
    password.send_keys("787898@OkOk", Keys.RETURN)
    contact_us = driver.find_element(By.XPATH, '/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a')
    contact_us.click()

print(process())



