from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import textToSpeech

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictRoute():
    data = request.json['data']
    result = textToSpeech.text2Speech(data)
    return {"data": result.decode("utf-8")}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
