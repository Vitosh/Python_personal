import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_update_item(client):
    # Setup: create a new item
    client.post('/api/items', json={'name': 'Test Item1'})
    client.post('/api/items', json={'name': 'Test Item2'})
    client.post('/api/items', json={'name': 'Test Item3'})

    # Test update 
    update_response = client.put('/api/items/2', json={'item':{"name":'Updated Test Item2'}})
    assert update_response.status_code == 200
    assert update_response.json['item']['name'] == 'Updated Test Item2'

    # Cleanup: delete the item
    client.delete('/api/items/1')
    client.delete('/api/items/2')
    client.delete('/api/items/3')


def test_delete_item(client):
    client.post('/api/items', json={'name': 'Test Item4'})

    delete_response = client.delete('/api/items/1')
    assert delete_response.status_code == 200

    get_response = client.get('/api/items/1')
    assert get_response.status_code == 404

