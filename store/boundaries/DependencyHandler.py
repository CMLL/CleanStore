from AbstractInjector import InjectorInterface
from store.users import UserManager
from store.boundaries.SQLImplementation import SQLAlchemyImplementation


class UserInjector(InjectorInterface):

    def get_manager(self):
        """
        Return a manager to perform operations on users.
        """
        database_repo = SQLAlchemyImplementation()
        manager = UserManager(user_repository=database_repo)
        return manager
