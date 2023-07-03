# https://requests.readthedocs.io/en/latest/user/advanced/#custom-authentication
import requests
from requests.auth import AuthBase


class TestAuth(AuthBase):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __call__(self, req: requests.Request):
        req.headers["username"] = self.username
        req.headers["password"] = self.password
        return req


url = "https://httpbin.org/post"
resp = requests.post(url=url, auth=TestAuth("User", "12345"))
print(resp.url)
print(resp.headers)
print(resp.text)

