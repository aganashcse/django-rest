import requests
from requests.auth import HTTPBasicAuth

#For getting jwt token
passwd = "1"
x = requests.post(url='http://127.0.0.1:8000/api/token/', data={"username":"ganesh", "password":passwd})

print(x.text)


#After getting jwt token, need to add the token in headers for authorization
headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3ODU4NTcwLCJqdGkiOiI0YzQyMzk5MjA5MTE0NDAwYmViNDQ3NTZiMGYwMTAwZCIsInVzZXJfaWQiOjF9.wvS53HjN3cFK6RGugtlQ-KskEsIhL33PQFe3yhr9Gd'
r = requests.get(url="url", headers=headers)
print(r.text)