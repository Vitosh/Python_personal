import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_cube_endpoint(self):
        data = {"number": 5}
        response = self.app.post('/api/cube', json=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['result'], 125)

    def test_cube_negative_number(self):
        data = {"number": -3}
        response = self.app.post('/api/cube', json=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['result'], -27)

    def test_cube_missing_number(self):
        data = {}
        response = self.app.post('/api/cube', json=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', result)
    
if __name__ == '__main__':
    unittest.main()
    