

def check_method_if_exists(all_methods, to_be_executed):
    for i in to_be_executed:
        for key, value in i.items():
            if key == 'and':
                for method in all_methods:
                    if value == method:
                        i[key] = method
    return to_be_executed
