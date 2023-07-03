# https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
import requests
requests.get('https://github.com/', timeout=0.001)
