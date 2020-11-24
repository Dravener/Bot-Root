import re

from difflib import SequenceMatcher


def scrape_elements(previous_function, all_methods, user_input):
    elements = previous_function.find_elements_by_tag_name('*')  # find all elements on this page
    previous_element = ''
    for index in range(len(elements)):  # loop through those elements
        if elements[index].tag_name == 'html' or elements[index].tag_name == 'body':
            pass
        else:
            if elements[index].text == previous_element:  # check if element text is same with previous element
                pass
            else:
                el = re.search(r'def\s*.*\(.*\)\:', elements[index].text)  # search for string
                if el is not None:
                    current_element = all_methods[user_input](elements[index].text)
                    seq = SequenceMatcher(a=previous_element, b=current_element['text'])  # get matching ratio
                    if seq.ratio() < 0.81:
                        if current_element['nam'] != '' and current_element['text'] != '':
                            items = {"text": current_element['text']}
                            return items
                        else:
                            print('Empty t: ' + str(index))
                    else:
                        pass
                    previous_element = current_element['text']
