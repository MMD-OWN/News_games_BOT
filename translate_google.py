import requests
import time
import os

my_secret = os.getenv('TEST_BOT')

def translate(lan, text):
    time.sleep(0.1)
    if text == '' or text == ' ':
        return ''
    data = {
        "target": lan,
        "text": text
    }
    headers = {
        'accept': 'application/json',
        'one-api-token': my_secret,
        'Content-Type': 'application/json'
    }
    response = requests.post('https://api.one-api.ir/translate/v1/yandex/', json=data, headers=headers)
    return response.json()['result']
