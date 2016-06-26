from flask import Flask
from flask_restful import Api


StoreApi = Flask(__name__)
api = Api(StoreApi)


from controllers.users_controllers import UserController


api.add_resource(UserController, '/users', endpoint='users')
