from store.users.Manager import UserManager
from store.users.Model import User


class TestUsers:

    def test_username_and_password_are_needed_to_create_new_user(self):
        user = User(username='name', password='password')

        assert user.username == 'name'
        assert user.password == 'password'
