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
from pytesseract import Output
import pandas as pd
from PIL import Image
import os
import requests
import json
from main_scripts.python_format import python_format
import cv2
from difflib import SequenceMatcher


def write(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    f = open(file_name, "w+")
    f.write(text_to_append)
    f.close()


def create_bit(title, content, user_id):
    subject = 'Python'
    url = 'https://bitsapiforbytes.herokuapp.com/extension_bit_create'
    body = {
        "title": title,
        "subject": subject,
        "content": content,
        "user_id": user_id,
        "public": True
    }
    headers = {'content-type': 'application/json'}
    req = requests.post(url, data=json.dumps(body), headers=headers)
    infos = json.loads(req.text)
    print(infos)


def open_chrome_and_visit_bing(query, token, user_id):
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
    elem.send_keys(query)  # type query in the search bar
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

    final_text = open_links(links, query, token, user_id)  # pass links and search query to openLinks method
    driver.quit()
    os.remove("screenshot1.png")  # delete image(screenshot)
    return final_text


def open_links(links, query, token, user_id):
    print(links)
    links_length = len(links)  # length of the links array
    items = {}  # init dictionary
    text_to_be_summarized = ''  # init empty string variable
    for i in range(0, links_length):
        print('New Page ==========================')
        text_for_each_page = ''
        options = ChromeOptions()
        options.add_argument('start-maximized')
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        try:  # try to open link in browser ( some links are 'broken' that's why try and except)
            driver.get(links[i])
            wait = WebDriverWait(driver, 10)  # init wait time for driver
            men_menu = wait.until(ec.visibility_of_element_located((By.TAG_NAME, 'body')))
            time.sleep(2)
            elements = driver.find_elements_by_tag_name('*')  # find all elements on this page
            previous_element = ''
            for index in range(len(elements)):  # loop through those elements
                if elements[index].tag_name == 'html' or elements[index].tag_name == 'body':
                    pass
                else:
                    if elements[index].text == previous_element: # check if element text is same with previous element
                        pass
                    else:
                        el = re.search(r'def\s*.*\(.*\)\:', elements[index].text)  # search for string
                        if el is not None:
                            current_element = python_format(elements[index].text, elements[index].tag_name)
                            seq = SequenceMatcher(a=previous_element, b=current_element['text']) # get matching ratio
                            if seq.ratio() < 0.81:
                                if current_element['nam'] != '' and current_element['text'] != '':
                                    create_bit(current_element['nam'], current_element['text'], user_id)
                                else:
                                    print('Empty t: ' + str(i))
                            else:
                                pass
                            previous_element = current_element['text']
                            text_for_each_page += current_element['text']
                            text_to_be_summarized += current_element['text']
            website_title = driver.title
            items[website_title] = text_for_each_page  # dictionary :=>  key: page_name value: page text
        except WebDriverException:
            print('error')
        driver.quit()
    summarized_text = summarize(text_to_be_summarized, ratio=0.9)  # summarize the text from all domains
    final_summarized_text = summarize(summarized_text, ratio=0.9)  # summarize the text from all domains
    items['summary'] = final_summarized_text
    return items
