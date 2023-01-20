import unittest
import app


class TestAPI(unittest.TestCase):

    def setUp(self):
        # create a test client
        self.client = app.app.test_client()

    def test_start(self):
        # send a POST request to the /start endpoint
        response = self.client.post('/start', json={'player1': 'Alice', 'player2': 'Bob'})
        # check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)
        # check that the response has the correct message
        self.assertEqual(response.get_json()['message'], 'Game started')

    def test_play(self):
        # send a POST request to the /play endpoint
        response = self.client.post('/play', json={'player1': 'rock', 'player2': 'scissors'})
        # check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)
        # check that the response has the correct result
        self.assertEqual(response.get_json()['result'], 'Alice wins')

    def test_score(self):
        # send a GET request to the /score endpoint
        response = self.client.get('/score')
        # check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)
        # check that the response has the correct score
        self.assertEqual(response.get_json()['player1'], 'Alice: 0')
        self.assertEqual(response.get_json()['player2'], 'Bob: 0')


if __name__ == '__main__':
    unittest.main()
