import glob
import importlib
import inspect
import json
import os
import time
from time import ctime
import requests

for filename in glob.glob("audio*"):
    os.remove(filename)

token = ''
user_id = ''
all_files = {}
imp_modules = []
all_methods = {}


def import_all_functions():
    all_files["package"] = os.listdir('package')
    all_files["main_scripts"] = os.listdir('main_scripts')
    for key, value in enumerate(all_files, start=0):
        for file in all_files[value]:
            if not file.startswith('__'):
                path = f'{value}/{file}'
                if os.path.isdir(path):
                    files_in_directory = os.listdir(path)
                    for item in files_in_directory:
                        if not item.startswith('__'):
                            name = item.split('.')
                            plugin = f"{value}.{file}.{name[0]}"
                            imp_modules.append(importlib.import_module(plugin, "."))
                else:
                    name = file.split('.')
                    plugin = f"{value}.{name[0]}"
                    imp_modules.append(importlib.import_module(plugin, "."))
        # fill the dictionary with functions name as key and the actual function as value
        for index, module in enumerate(imp_modules, start=0):
            module_methods = dir(module)
            for item in module_methods:
                if not item.startswith('_'):
                    all_methods[item] = imp_modules[index].__getattribute__(item)
    print(all_methods.keys())


def login():
    global token, user_id
    url = 'https://bitsapiforbytes.herokuapp.com/extension_login'
    body = {"user": {
        "email": "dravener@gmail.com",
        "password": "papaki1"
    }}
    headers = {'content-type': 'application/json'}
    req = requests.post(url, data=json.dumps(body), headers=headers)
    infos = json.loads(req.text)
    print(infos)
    token = infos["token"]
    user_id = infos["userId"]


previous_function = None
import_all_functions()
time.sleep(1)
# all_methods['gueno_speak']("Hello Captain")
while 1:
    # voice_data = all_methods['record_audio'](all_methods['gueno_speak'])
    print(previous_function)
    search = input("Enter your command: ")
    previous_function = all_methods["respond"](previous_function, all_methods, search)
