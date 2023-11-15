import os
import unittest
import requests
from dotenv import load_dotenv
import json
from pprint import pprint as pp

YA_BASE_URL = 'https://cloud-api.yandex.net'
load_dotenv()
YA_TOKEN = os.getenv('TOKEN_YA')
def create_folder():
    url = f'{YA_BASE_URL}/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
               'Authorization': YA_TOKEN}
    params = {'path': 'UnittestFolder',
              'overwrite': 'false'}
    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code

pp(create_folder())

