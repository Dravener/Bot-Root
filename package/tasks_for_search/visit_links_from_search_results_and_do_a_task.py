from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


def open_links(previous_function, all_methods, user_input=False):
    links_length = len(previous_function)  # length of the links array
    task_result = []
    for i in range(0, links_length):
        options = ChromeOptions()
        options.add_argument('start-maximized')
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        try:  # try to open link in browser ( some links are 'broken' that's why try and except)
            driver.get(previous_function[i])
            wait = WebDriverWait(driver, 10)  # init wait time for driver
            wait.until(
                ec.visibility_of_element_located((By.TAG_NAME, 'body')))  # WebDriver wait body element appearance
            time.sleep(2)
            method = all_methods[user_input["and"]](driver, all_methods, user_input["with"])  # Apply TASK to each link
            if method is not None:
                task_result.append(method)  # Append TASK result to array
        except WebDriverException:
            print('error')
        driver.quit()
    return task_result
