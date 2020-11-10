from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from gensim.summarization import summarize
import re
import pytesseract
from PIL import Image
import os



def openChromeAndVisitBing(query):
    # driver options ========
    options = ChromeOptions()
    options.add_argument('start-maximized')
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)
    # driver options ==========
    driver.get('https://www.bing.com')
    wait = WebDriverWait(driver, 10)
    # wait for pop up to appear then click on it
    men_menu = wait.until(ec.visibility_of_element_located((By.ID, 'bnp_btn_accept')))
    # click the button that appears in the pop up
    men_menu.click()
    # find search bar
    elem = driver.find_element_by_name("q")
    elem.clear()
    # type query in the search bar
    elem.send_keys(query)
    # hit enter
    elem.send_keys(Keys.RETURN)
    # wait for page to load
    time.sleep(5)
    # find lists that contains elements with the links
    boDy = driver.find_element_by_id('b_results')
    # change window dimensions to cover whole screen and the get a screenshot
    total_height = boDy.size["height"] + 1000
    driver.set_window_size(1920, total_height)
    time.sleep(2)
    # save screenshot
    driver.save_screenshot("screenshot1.png")
    # open image(screenshot)
    img = Image.open('screenshot1.png')
    # extract its string
    image_text = pytesseract.image_to_string(img)
    # find all links from extracted image text
    links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[.]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', image_text)
    # pass links and search query to openLinks method
    finalText = openLinks(links, query)
    driver.quit()
    # delete image(screenshot)
    os.remove("screenshot1.png")
    return finalText


def openLinks(links, query):
    print(links)
    # length of the links array
    links_length = len(links)
    # init dictionary
    items = {}
    # init empty string variable
    text_to_be_summarized = ''
    for i in range(0, links_length):
        text_for_each_page = ''
        options = ChromeOptions()
        options.add_argument('start-maximized')
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        # try to open link in browser ( some links are 'broken' that's why try and except)
        try:
            driver.get(links[i])
            # find all elements in page
            elements = driver.find_elements_by_css_selector('*')
            for element in elements:
                # check if element has text
                if not element.text:
                    text_to_be_summarized += ''
                else:
                    text_to_be_summarized += element.text
                    text_for_each_page += element.text
        except WebDriverException:
            print('error')
        # add item to dictionary with domain as key and it's text as value
        items['%s' % links[i]] = text_for_each_page
        driver.quit()
    # summarize the text from all domains
    summarized_text = summarize(text_to_be_summarized, ratio=0.3)
    final_summarized_text = summarize(summarized_text, ratio=0.1)
    items['summary'] = final_summarized_text
    return items
