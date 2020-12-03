

def select_element(previous_function, all_methods, user_input):
    txt = ''
    new_query = txt.join(user_input["vars"])

    el = previous_function.find_element_by_tag_name(f'n{new_query}')
    print(el)
