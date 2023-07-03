# https://requests.readthedocs.io/en/latest/user/quickstart/#cookies
import requests
# get cookies
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
# print(r.cookies['example_cookie_name'])

# send cookies
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
print(r.text)

