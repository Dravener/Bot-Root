

def go_back(previous_function, all_methods, user_input):
    # print(previous_function)
    if previous_function is not None:
        previous_function.back()
        return previous_function
