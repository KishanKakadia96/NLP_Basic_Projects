from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
import os
import speechTotext
from src.utils import decodeSound


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['sound']
    decodeSound(image, "audio123.wav")
    result = speechTotext.speech2Text("audio123.wav")
    return jsonify({"Result": str(result)})



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
