from flask_restful import Resource
from flask import request
from store.boundaries import UserInjector


class UserController(Resource):

    def post(self):
        # Load up the information. Related to the ui.
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Manager for dependencies. That way, ui doesn't need to
        # know of the creation process of domain objects. That's way to
        # specific.
        injector = UserInjector()
        # He just get a domain object with a specific interface.
        # Use it and complies with the result.
        user_manager = injector.get_manager()

        user = user_manager.create_new_user(username, password)
        return {'id': user.id, 'username': user.username}, 201
