from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time


def click():
    cookie_clicker = driver.find_element(By.CSS_SELECTOR, '#cookie')
    cookie_clicker.click()


ser = Service("C:/Users/Pc/Downloads/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


def get_store():
    store = driver.find_elements(By.CSS_SELECTOR, '#store b')
    items_id = driver.find_elements(By.CSS_SELECTOR, '#store div')
    return store, items_id


def get_upgrades():
    upgrades = {}
    for n in range(len(price)):
        upgrades[price[n]] = ids[n]
    return upgrades


def get_price_list():
    price_list = []
    for item in store:
        element_text = item.text
        print(element_text)
        if element_text != "":
            prices = element_text.split('-')[1].strip().replace(',', '')
            price_list.append(prices)
    return price_list


def get_ids():
    ids = []
    for id in items_id:
        item = id.get_attribute('id')
        ids.append(item)
    del ids[-1]
    return ids


dont_stop = True
while dont_stop:
    store, items_id = get_store()
    price = get_price_list()
    ids = get_ids()
    cookie_upgrades = get_upgrades()
    click()
    cookie = driver.find_element(By.CSS_SELECTOR, '#money')
    cookie_money = int(cookie.text)
    for key, value in cookie_upgrades.items():
        if cookie_money > int(key):
            get_upgrade = driver.find_element(By.CSS_SELECTOR, f'#store #{cookie_upgrades[key]}')
            get_upgrade.click()
            print(f'bought {cookie_upgrades[key]}')
            time.sleep(2)
        else:
            break

    print(price)

driver.quit()
