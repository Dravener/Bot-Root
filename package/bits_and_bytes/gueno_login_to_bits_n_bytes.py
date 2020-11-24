import json

import requests


def bnb_login(previous_function, all_methods, user_input):
    url = 'https://bitsapiforbytes.herokuapp.com/extension_login'
    body = {"user": {
        "email": f'{user_input["vars"][0]}',
        "password": f'{user_input["vars"][1]}'
    }}
    headers = {'content-type': 'application/json'}
    req = requests.post(url, data=json.dumps(body), headers=headers)
    infos = json.loads(req.text)
    print(infos)
    return infos
