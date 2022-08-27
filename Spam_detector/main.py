from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    data = request.json["data"]
    p = prediction(data)
    print(p)
    print(type(p))
    return {"Result": str(p)}




if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=5000, debug=True)