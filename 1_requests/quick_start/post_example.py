# https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests
import requests
payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

# https://requests.readthedocs.io/en/latest/user/quickstart/#post-a-multipart-encoded-file
url = 'https://httpbin.org/post'
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
r = requests.post(url, files=files)
print(r.text)
