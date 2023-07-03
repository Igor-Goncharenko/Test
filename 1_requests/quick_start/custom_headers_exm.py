# https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers
import requests
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
