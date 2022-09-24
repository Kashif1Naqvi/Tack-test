import requests


url = "http://127.0.0.1:8000/auth/register/"

body = {
    "username": "aaaaa",
    "password": "testing123",
    "first_name": "syed",
    "last_name": "slaman",
    "email": "aaaaaaaa@gmail.com",
    "gender": "male",
    "country": "pakistan",
    "nationality": "pakistani"
}



requests.post(url,  json=body)



# login_url = "http://127.0.0.1:8000/auth/login/"


# body = {
#     "username": "salmanss",
#     "password": "testing123",
#  }
