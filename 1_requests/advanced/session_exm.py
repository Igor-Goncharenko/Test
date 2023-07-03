# https://requests.readthedocs.io/en/latest/user/advanced/#session-objects
import requests
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)
# with requests.Session() as s:
#     s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
# both 'x-test' and 'x-test2' are sent
r = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
