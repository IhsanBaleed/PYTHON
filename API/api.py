from flask import Flask, jsonify, request
from functions import *

# this is a rest API server
app = Flask(__name__)

data = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"},
    {"id": 3, "name": "Item Three"},
    {"id": 4, "name": "Item Four"},
]

@app.route('/')
def home():
    return jsonify({"message": "Hello World"})

@app.route('/Func1')
def Func1_call():
    return Func1()

@app.route('/Func2')
def Func2_call():
    return Func2()

@app.route('/Func3')
def Func3_call():
    return Func3()

@app.route('/items', methods=['GET'])
def get_items():
    name_filter = request.args.get('name')  # optional query param ?name=Item
    limit = request.args.get('limit', type=int)  # optional query param ?limit=2

    filtered = data
    if name_filter:
        filtered = [item for item in filtered if name_filter.lower() in item['name'].lower()]
    
    if limit:
        filtered = filtered[:limit]

    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)