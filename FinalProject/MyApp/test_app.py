import unittest
from app import connex_app
import json


BASE_DIRECTORS_URL = '/api/directors'
GET_DIRECTORS_LIMIT = '{}-filter/3/desc/id'.format(BASE_DIRECTORS_URL)
GET_DIRECTORS_ONE = '{}/7110'.format(BASE_DIRECTORS_URL)
GET_DIRECTORS_NOT_FOUND = '{}/-1'.format(BASE_DIRECTORS_URL)

BASE_MOVIES_URL = '/api/movies'
PUT_MOVIE_NOT_FOUND = '{}/7110/-1'.format(BASE_MOVIES_URL)
GET_MOVIE_FILTER = '{}-title/pirates'.format(BASE_MOVIES_URL)


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.connex_app = connex_app.app.test_client()
        self.connex_app.testing = True

    def test_get_directors(self):
        response = self.connex_app.get(BASE_DIRECTORS_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(data), list)

    def test_get_directors_limit(self):
        response = self.connex_app.get(GET_DIRECTORS_LIMIT)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_get_dirctors_one(self):
        response = self.connex_app.get(GET_DIRECTORS_ONE)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Brian Herzlinger')
        self.assertEqual(type(data), dict)

    def test_directors_one_not_found(self):
        response = self.connex_app.get(GET_DIRECTORS_NOT_FOUND)
        self.assertEqual(response.status_code, 404)

    def test_create_director(self):
        director = {
            "department": "string",
            "gender": 0,
            "name": "string",
            "uid": 1
        }
        response = self.connex_app.post(BASE_DIRECTORS_URL, data=json.dumps(
            director), content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_movie_update_not_found(self):
        response = self.connex_app.put(PUT_MOVIE_NOT_FOUND)
        self.assertEqual(response.status_code, 404)

    def test_movie_delete_not_found(self):
        response = self.connex_app.delete(PUT_MOVIE_NOT_FOUND)
        self.assertEqual(response.status_code, 404)

    def test_get_movies_filter(self):
        response = self.connex_app.get(GET_MOVIE_FILTER)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 7)


if __name__ == '__main__':
    unittest.main()
