"""
Run this test with: pytest -vs request_test.py
-v means: verbose
-s means: print custom messages to the console
"""

import unittest
import requests

# url = 'http://localhost:5000'
url = 'http://localhost:8000'
token = ''
test_id = None


class TestApi(unittest.TestCase):
    # def test_01_home(self):
    #     res = requests.get(url).json()
    #     assert res == {'message': 'Welcome'}

    def test_05_post_snippet(self):
        global test_id
        req = {'code': 'print("ho")'}
        res = requests.post(url + '/snippets', json=req).json()
        test_id = res['id']
        assert res['code'] == 'print("ho")'

    def test_06_put_snippet(self):
        req = {'code': 'print("haha")'}
        res = requests.put('{}/snippets/{}'.format(url, test_id), json=req).json()
        assert res['code'] == 'print("haha")'

    def test_07_get_snippet(self):
        res = requests.get('{}/snippets/{}'.format(url, test_id)).json()
        assert res['code'] == 'print("haha")'

    def test_08_get_snippets(self):
        res = requests.get(url + '/snippets').json()
        assert len(res) > 0

    def test_09_delete_snippet(self):
        res = requests.delete('{}/snippets/{}'.format(url, test_id))
        assert res.status_code == 204

