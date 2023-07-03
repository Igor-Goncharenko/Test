# https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
import requests

r = requests.get('https://api.github.com/events')
r.json()