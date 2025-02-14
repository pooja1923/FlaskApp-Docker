from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a + b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a - b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({'result': a * b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 1))
        if b == 0:
            return jsonify({'error': 'Division by zero'}), 400
        return jsonify({'result': a / b})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
