

def does_gueno_have_func_with_name(function_name, function_list):
    has_functions = []
    for function in function_list:
        if function_name in function:
            has_functions.append(function)
    return has_functions
