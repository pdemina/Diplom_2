import helper_user
import allure
import pytest
from faker import Faker


class TestUserCreation:

    @allure.title('Создание пользователя проходит успешно')
    @allure.description('Проверяем, что после создания пользователя воозвращается код 200')
    def test_user_creation(self):
        fake = Faker()
        email = fake.first_name() + "@yandex.ru"
        password = fake.last_name()
        name = fake.first_name()
        response = helper_user.create_user(email, password, name)
        helper_user.delete_user(email, password)
        assert response.status_code == 200

    @allure.title('Создание пользователя который уже зарегестрирован')
    @allure.description('Проверяем, что после повторного создания воозвращается код 403')
    def test_user_creation(self):
        fake = Faker()
        email = fake.first_name() + "@yandex.ru"
        password = fake.last_name()
        name = fake.first_name()
        response = helper_user.create_user(email, password, name)
        response = helper_user.create_user(email, password, name)
        helper_user.delete_user(email, password)
        assert response.status_code == 403

    @allure.title('Создание пользователя с пустыми обязательными полями приводит к ошибке')
    @allure.description('Проверяем, что при пустых обязательных полях сообщение "Email, password and name are required fields"')
    def test_user_creation(self):
        response = helper_user.create_user('', '', '')
        assert 'Email, password and name are required fields' in response.text

