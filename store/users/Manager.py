from store.users.Model import User

class UserManager(object):

    def __init__(self, user_repository):
        self._repository = user_repository

    def create_new_user(self, username, password):
        new_user = User(username, password)
        database_user = self._repository.save(new_user)
        new_user.id = database_user.id
        return new_user
