from api import StoreApi
from pytest import fixture
from json import loads, dumps

@fixture
def client():
    return StoreApi.test_client()


class TestUsers:

    headers = {'Content-Type': 'application/json'}

    def test_user_endpoint_receives_correct_user_info_via_the_api_should_get_correct_status(self, client):
        username = 'username'
        password = 'password'
        formatted_data = dumps(dict(username=username, password=password))

        response = client.post('/users', data=formatted_data, headers=self.headers)
        returned_data = loads(response.data)

        assert response.status_code == 201
        assert 'username' in returned_data
        assert 'id' in returned_data

