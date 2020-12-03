import time

import pyautogui
from selenium.common.exceptions import StaleElementReferenceException


def click_video(previous_function, all_methods, user_input):
    txt = ' '
    new_query = txt.join(user_input["vars"])
    if previous_function is not None:
        elements = previous_function.find_element_by_id('contents')  # find all elements on this page
        children = elements.find_elements_by_xpath('./child::*')
        for element in children:
            if new_query != '' and new_query in element.text:
                loc = element.location
                # print(new_query)
                # print(loc)
                # print(element.text)
                pyautogui.moveTo(loc['x'] + 50, loc['y'] + 320)
                time.sleep(5)
                pyautogui.click()
    return previous_function
