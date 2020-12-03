

def go_forward(previous_function, all_methods, user_input):
    if previous_function is not None:
        previous_function.forward()
        return previous_function
