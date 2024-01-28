import pytest
import helper_user


@pytest.fixture
def user_fixture():
    user = helper_user.create_user_with_unique_data()
    yield user
    helper_user.delete_user(user[0], user[1])


