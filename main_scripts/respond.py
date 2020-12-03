import inspect

from main_scripts.command_pipe_line import command_pipe_line


# from main_scripts.check_method_if_exists import check_method_if_exists


def respond(previous_function, all_methods, voice_data):
    commands = voice_data.split('then')
    to_be_executed = command_pipe_line(commands)
    # to_be_executed = check_method_if_exists(all_methods, to_be_executed)
    previous_function = previous_function
    for index in range(len(to_be_executed)):
        for key, value in to_be_executed[index].items():
            # arg = inspect.signature(all_methods[key]).parameters["previous_function"].annotation
            # prev_arg = type(previous_function)
            # if previous_function is not None and prev_arg != arg:
            #     previous_function = arg(previous_function)
            previous_function = all_methods[key](previous_function, all_methods, value)

    if previous_function is not None:
        return previous_function
