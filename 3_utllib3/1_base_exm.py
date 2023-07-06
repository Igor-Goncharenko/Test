import urllib3


http = urllib3.PoolManager()
url = 'http://webcode.me'
resp = http.request('GET', url)
print(resp.status)
for key, value in resp.headers.items():
    print(f"{key}: {value}")
# print(resp.data.decode('utf-8'))

