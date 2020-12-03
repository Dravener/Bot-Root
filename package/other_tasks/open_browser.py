from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pyautogui
import time
import pytesseract
from PIL import Image
import os


def open_browser(previous_function, all_methods, user_input):
    txt = ''
    new_query = txt.join(user_input["vars"])
    options = ChromeOptions()  # driver options ========
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument('start-maximized')
    options.headless = False
    driver = webdriver.Chrome(chrome_options=options)  # driver options ==========
    driver.get(f'https://www.{new_query}.com')
    # time.sleep(5)
    wait = WebDriverWait(driver, 10)  # wait for pop up to appear then click on it
    men_menu = wait.until(ec.visibility_of_element_located((By.ID, 'dialog')))

    loc = men_menu.location
    # print(loc)
    pyautogui.moveTo(loc['x'] + 90, loc['y'] + 450)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(loc['x'] + 250, loc['y'] + 540)
    pyautogui.click()
    time.sleep(2)
    # # men_menu.click()  # click the button that appears
    return driver
