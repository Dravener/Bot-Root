import time

import pyautogui


def scroll_down(previous_function, all_methods, user_input):
    time.sleep(5)
    pyautogui.scroll(-10)
    return previous_function
