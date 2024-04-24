import requests
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_new_user():
    login_pass = []

    email = f'{generate_random_string(6)}@ya.ru'
    password = generate_random_string(10)
    name = generate_random_string(5)

    payload = {
        "email": email,
        "password": password,
        "name": name
        }

    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        token = response.json()['accessToken']

    return login_pass, token
