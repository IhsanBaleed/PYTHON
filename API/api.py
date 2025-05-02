from flask import Flask, jsonify
from functions import *

app = Flask(__name__)

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

@app.route('/items/<int:item_id>')
def get_item(item_id):
    return jsonify({"item_id": item_id})

if __name__ == '__main__':
    app.run(debug=True)