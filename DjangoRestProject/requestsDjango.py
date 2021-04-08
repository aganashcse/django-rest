import requests
from requests.auth import HTTPBasicAuth

passwd = "1"
x = requests.post(url='http://127.0.0.1:8000/api/token/', data={"username":"ganesh", "password":passwd})

print(x.text)