import requests
import allure
import urls
from faker import Faker


def create_authorization_header(access_token):
    header = {"authorization": access_token}
    return header


@allure.step('Создаем пользователя')
def create_user(email, password, name):
    payload = {'email': email, 'password': password, 'name': name}
    response = requests.post(urls.BASE_URL + urls.USER_REGISTRATION, payload)
    return response


@allure.step('Логин пользователя')
def login_user(email, password):
    payload = {'email': email, 'password': password}
    response = requests.post(urls.BASE_URL + urls.USER_LOGIN, payload)
    return response


def get_access_token(response):
    access_token = response.json()['accessToken']
    return access_token


@allure.step('Изменение email пользователя')
def patch_user_email(access_token, email):
    header = create_authorization_header(access_token)
    payload = {'email': email}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


@allure.step('Изменение password пользователя')
def patch_user_password(access_token, password):
    header = create_authorization_header(access_token)
    payload = {'password': password}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


@allure.step('Изменение name пользователя')
def patch_user_name(access_token, name):
    header = create_authorization_header(access_token)
    payload = {'name': name}
    response = requests.patch(urls.BASE_URL + urls.USER_AUTH_USER, headers=header, data=payload)
    return response


def create_user_with_unique_data():
    email_pass = []
    fake = Faker()
    email = fake.first_name() + "@yandex.ru"
    password = fake.last_name()
    name = fake.first_name()
    response = create_user(email, password, name)
    if response.status_code == 200:
        email_pass.append(email)
        email_pass.append(password)
        email_pass.append(name)
    return email_pass


def delete_user(email, password):
    response = login_user(email, password)
    access_token = get_access_token(response)
    header = create_authorization_header(access_token)
    delete_response = requests.delete(urls.BASE_URL + urls.USER_AUTH_USER, headers=header)






