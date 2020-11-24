

def save_bits(previous_function, all_methods, user_input=False):
    text = ''
    for i in previous_function:
        for key, value in i.items():
            text += value
    file_name = ''
    for item in user_input["vars"]:
        file_name += item
    f = open(file_name, "w+")
    f.write(text)
    f.close()
