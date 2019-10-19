from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

name = "Nitish Jadia"

@app.route('/api/v1.0/name', methods=['GET'])
def getName():
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run(debug=True)