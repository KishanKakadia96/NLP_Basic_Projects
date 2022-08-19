from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS, cross_origin

app=Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
cross_origin()
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
cross_origin()
def predict():
    pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
