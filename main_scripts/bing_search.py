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


def bing_search(previous_function, all_methods, user_input=False):
    txt = ''
    new_query = txt.join(user_input["vars"])  # Arrays to String
    options = ChromeOptions()  # driver options ========
    options.add_argument('start-maximized')
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)  # driver options ==========
    driver.get('https://www.bing.com')
    wait = WebDriverWait(driver, 10)  # wait for pop up to appear then click on it
    men_menu = wait.until(ec.visibility_of_element_located((By.ID, 'bnp_btn_accept')))
    men_menu.click()  # click the button that appears in the pop up
    elem = driver.find_element_by_name("q")  # find search bar
    elem.clear()
    elem.send_keys(new_query)  # type query in the search bar
    elem.send_keys(Keys.RETURN)  # hit enter
    time.sleep(5)  # wait for page to load
    bo_dy = driver.find_element_by_css_selector('body')  # find body element
    total_height = bo_dy.size["height"] + 1000  # change body's element dimensions
    driver.set_window_size(1920, total_height)
    time.sleep(2)
    driver.save_screenshot("screenshot1.png")  # save screenshot
    img = Image.open('screenshot1.png')  # open || read  image(screenshot)
    image_text = pytesseract.image_to_string(img)  # extract  string from image
    tech = image_text.splitlines()  # split text from image
    links = []
    for sent in tech:
        if sent.startswith('http'):  # find all links from extracted image text
            links.append(sent[:-2])
    driver.quit()
    os.remove("screenshot1.png")  # delete image(screenshot)
    return links
