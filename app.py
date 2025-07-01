from flask import Flask, jsonify, request
from flask_cors import CORS  # 추가

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Flask API is running!'

@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello from Flask!',
        'status': 'success'
    })

@app.route('/api/add', methods=['GET'])
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({
        'a': a,
        'b': b,
        'result': a + b
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'you_sent': data
    })
