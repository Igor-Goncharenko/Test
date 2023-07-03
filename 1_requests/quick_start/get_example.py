import requests
r = requests.get('https://www.python.org')
print(f"{r.content=}")
print(f"{r.request=}")
print(f"{r.url=}")
print(f"{r.headers=}")
print(f"{r.apparent_encoding=}")
print(f"{r.cookies=}")
print(f"{r.elapsed=}")
print(f"{r.encoding=}")
print(f"{r.history=}")
print(f"{r.links=}")
print(f"{r.is_permanent_redirect=}")
print(f"{r.is_redirect=}")
print(f"{r.reason=}")
print(f"{r.status_code=}")
# print(r.json())


