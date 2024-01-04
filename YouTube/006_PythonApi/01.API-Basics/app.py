from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/testapi', methods=['POST'])
def testapi():
    data = request.get_json()
    print(f'{data}{data}')
    return f'{data}{data}'

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({'error':'Required - name!'}), 400

    name = data['name']
    greeting = f"Hello, there - {name}!"

    return jsonify({'message':greeting})

@app.route('/api/cube', methods=['POST'])
def cube():
    data = request.get_json()
    #print("\nMultiplying 3 times the same value!")
    if 'number' not in data:
        return jsonify({'error':'Required - number!'}), 400

    number = data['number']
    result = number ** 3

    return jsonify({'result': result})


@app.route('/api/concat', methods=['POST'])
def concat():
    data = request.get_json()

    if ('string1' not in data) or ('string2' not in data):
        return jsonify({'error':'Required - string1 and string2!'}), 400

    string1 = data['string1']
    string2 = data['string2']
    result = string1 + string2

    return jsonify({'result': result})



if __name__ == '__main__':
    app.run(debug=True)
