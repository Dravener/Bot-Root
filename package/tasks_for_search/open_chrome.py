import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
import pytesseract
from PIL import Image
import os


def open_chrome(previous_function, all_methods, user_input):
    options = ChromeOptions()  # driver options ========
    options.add_argument('start-maximized')
    options.headless = False
    driver = webdriver.Chrome(chrome_options=options)  # driver options ==========
    driver.get('https://www.google.com/')
    return driver
