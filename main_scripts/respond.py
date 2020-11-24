
from main_scripts.command_pipe_line import command_pipe_line
# from main_scripts.check_method_if_exists import check_method_if_exists


def respond(all_methods, voice_data):
    commands = voice_data.split('then')
    to_be_executed = command_pipe_line(commands)
    # to_be_executed = check_method_if_exists(all_methods, to_be_executed)
    previous_function = None
    for index in range(len(to_be_executed)):
        for key, value in to_be_executed[index].items():
            previous_function = all_methods[key](previous_function, all_methods, value)

