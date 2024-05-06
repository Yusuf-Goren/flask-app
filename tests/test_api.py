import unittest
from flask import Flask

class TestFlaskApp(unittest.TestCase):

    def setUp(self):

        self.app = Flask(__name__)
        self.app.testing = True

    def test_post_request(self):
        with self.app.test_client() as client:
      
            response = client.get('/get-students')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()