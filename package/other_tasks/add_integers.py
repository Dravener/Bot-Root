

def add_integers(previous_function, all_methods, user_input):
    total = 0
    for num in user_input["vars"]:
        total += (int(num))
    all_methods["gueno_speak"](str(total))
