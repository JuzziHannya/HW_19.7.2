import requests

class TestApi:
    def test_get_api_key(self):
        body = {'email': 'qwe', 'password': 'qweqwe'}
        r = requests.get('https://petfriends.skillfactory.ru/api/key', params=body)
        assert r.status_code == 200