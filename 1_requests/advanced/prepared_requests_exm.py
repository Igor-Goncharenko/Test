# https://requests.readthedocs.io/en/latest/user/advanced/#prepared-requests
import requests


url = "https://httpbin.org/post"
headers = {}


with requests.Session() as s:
    req = requests.Request("POST", url=url, headers=headers)
    prepped = req.prepare()
    prepped.body = "I'm just request body."
    prepped.headers['Keep-Dead'] = 'parrot'
    resp = s.send(prepped)
    print(resp.content)

