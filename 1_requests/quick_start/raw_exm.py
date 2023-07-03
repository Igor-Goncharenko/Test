# https://requests.readthedocs.io/en/latest/user/quickstart/#raw-response-content
import requests
r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(10))

with open("test.txt", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
