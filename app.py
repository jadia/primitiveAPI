from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

name = "Nitish Jadia"

@app.route('/api/v1.0/name', methods=['GET'])
def getName():
    return jsonify({'name': name})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)