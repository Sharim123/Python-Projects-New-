# from bs4 import BeautifulSoup
# import requests
#
#
# url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
# content = requests.get(url).text
# #
# soup = BeautifulSoup(content, "html.parser")
# rate = soup.find('span', class_="stock-trend trend-drop").text
#
# print(rate)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


def get_driver():
    service = Service("C:/Users/shari/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def get_percentage():
    driver = get_driver()
    percentage = driver.find_element(By.CLASS_NAME, "stock-trend trend-drop")

    return percentage.text

print(get_percentage())

