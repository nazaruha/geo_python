from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_json/<string:filename>', methods=['GET'])
def get_json(filename):
    try:
        with open(filename + '.json', 'r') as file:
            json_data = file.read()
            return jsonify(json_data)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})

if __name__ == '__main__':
    app.run(debug=True)