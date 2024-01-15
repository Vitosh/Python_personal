from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database
items = []

# Create an item
@app.route('/api/items', methods = ['POST'])
def create_item():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Required - name!'}), 400
    
    item_id = len(items) + 1
    name = data['name']
    new_item = {'id':item_id, 'name':name}
    items.append(new_item)

    return jsonify({'message': 'Item created successfully', 'item': new_item}), 201

# Get all items
@app.route('/api/items', methods=['GET'])
def get_all_items():
    return jsonify({'items': items})

# Get item by ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({'error':f'Item {item_id} is not found, sorry!'}), 404
    return jsonify({'item':item})

# Get item by name
@app.route('/api/items/name/<string:item_name>', methods=['GET'])
def get_item_by_name(item_name):
    item = next((item for item in items if item['name'] == item_name), None)
    if item is None:
        return jsonify({'error':f'Item {item_name} is not found, sorry!'}), 404
    return jsonify({'item':item})

# Update item by id
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    updated_data = data.get('item') # Get the nested 'item' data

    if not updated_data:
        return jsonify({'error': 'No data provided'}), 400
    
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': f'Item #{item_id} not found!'})

    # Update fields in the item (dummy db)
    for key, value in updated_data.items():
        if key in item:
            item[key] = value

    return jsonify({'message': 'Item updated successfully', 'item':item}), 200


# Delete item by id
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item_to_delete = next((item for item in items if item['id'] == item_id), None)

    if item_to_delete is None:
        return jsonify({'error': f'Item {item_id} not found!'}), 404
    items.remove(item_to_delete)

    return jsonify({'message': f'Item: {item_to_delete} has been deleted successfully!'}), 200


if __name__ == '__main__':
    app.run(debug = True)