import helper_user
import allure
import data


class TestDataChanging:

    @allure.title('Изменение значения email пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_data_changing_with_authorization_successful(self):
        user = helper_user.create_user_with_unique_data()
        response = helper_user.login_user(user[0], user[1])
        access_token = helper_user.get_access_token(response)
        response = helper_user.patch_user_email(access_token, data.EXPECTED_EMAIL)
        helper_user.delete_user(data.EXPECTED_EMAIL, user[1])
        assert data.EXPECTED_EMAIL in response.text

    @allure.title('Изменение значения password пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_data_changing_with_authorization_successful(self):
        user = helper_user.create_user_with_unique_data()
        response = helper_user.login_user(user[0], user[1])
        access_token = helper_user.get_access_token(response)
        helper_user.patch_user_password(access_token, data.EXPECTED_PASSWORD)
        response = helper_user.login_user(user[0], data.EXPECTED_PASSWORD)
        helper_user.delete_user(user[0], data.EXPECTED_PASSWORD)
        assert response.status_code == 200

    @allure.title('Изменение значения name пользователя')
    @allure.description('Проверяем, что возможно изменение полей пользователя с авторизацией')
    def test_data_changing_with_authorization_successful(self):
        user = helper_user.create_user_with_unique_data()
        response = helper_user.login_user(user[0], user[1])
        access_token = helper_user.get_access_token(response)
        response = helper_user.patch_user_name(access_token, data.EXPECTED_NAME)
        helper_user.delete_user(user[0], user[1])
        assert data.EXPECTED_NAME in response.text
