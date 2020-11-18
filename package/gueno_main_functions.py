import json

import requests


def does_gueno_have_function(function_name, function_list, gueno_speak, inspect):
    answer = ''
    func_name = ''
    # iterate list with all the dictionary with function names as keys
    for key, value in function_list.items():
        # check if user input function name  string is contained in the keys
        if function_name in key:
            answer = 'yes'
            func_name = key
            break
        else:
            answer = 'no'
    # if function exists ( gueno has a function with a name containing that string) follow the commands
    if answer == 'yes':
        gueno_speak(f'Yes, i have a function with the name: {func_name}.')
        gueno_speak('Do you want me to show you the function?')
        user_answer = input("Enter your answer: ")
        if user_answer == 'yes':
            print(inspect.getsource(function_list[func_name]))
        else:
            gueno_speak('ok')
        gueno_speak('Do you want to use the function?')
        use_answer = input("Enter your answer: ")
        if use_answer == 'yes':
            var_a = input("Enter your variable A: ")
            var_b = input("Enter your variable B: ")
            print(function_list[func_name](int(var_a), int(var_b)))
        else:
            gueno_speak('ok')
    # if function does not exist ( gueno does not have a function with a name containing that string) follow the commands
    else:
        gueno_speak('No, i do not have that function.')
        gueno_speak('Do you want me to check if there is one on Bits and Bytes?')
        check_or_not = input("Yes or No?: ")
        if check_or_not == 'yes':
            url = 'https://bitsapiforbytes.herokuapp.com/search_title'
            body = {"q": function_name}
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(body), headers=headers)
            infos = json.loads(r.text)
            for key, element in enumerate(infos["allBits"]):
                print(key, element["content"])
            gueno_speak('Do you want me save any of those functions?')
            save_or_not = input('Yes or No: ')
            if save_or_not == 'yes':
                gueno_speak('The function with which index do you want to save?')
                function_index = input('Enter index number starting from 0: ')
                gueno_speak('Is this function the correct one?')
                print(infos['allBits'][int(function_index)]['content'])
                is_correct = input('is that the correct one? ')
                if is_correct == 'yes':
                    gueno_speak('cool')
                    append_new_line('./package/ex1.py', infos['allBits'][int(function_index)]['content'])
                else:
                    gueno_speak('ok')
        else:
            print('ok')


def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


