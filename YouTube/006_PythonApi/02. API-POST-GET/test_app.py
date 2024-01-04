import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_item(self):
        data = {'name':'New Item'}
        response = self.app.post('/api/items', json=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'], 'Item created successfully')

    def test_create_item_with_missing_name(self):
        data = {}
        response = self.app.post('/api/items', json=data)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', result)

    def test_get_all_items(self):
        response = self.app.get('/api/items')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', result)

    def test_create_items_and_get_count(self):
        response = self.app.get('/api/items')
        items_count = json.loads(response.data.decode('utf-8'))
        items_count_before_test = len(items_count.get('items',[]))

        # Create `n` additional items
        n = 5
        for i in range(n):
            data = {
                    'name': f'Item-{i+1}'
                    }
            self.app.post('/api/items', json=data)
        
        # Get all items:
        response = self.app.get('/api/items')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)

        # Check the if the count() is `n`:
        items_count = len(result.get('items', []))
        self.assertEqual(items_count, n + items_count_before_test)


if __name__ == '__main__':
    unittest.main()
    
