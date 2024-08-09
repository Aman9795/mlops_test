from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route("/", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.json
    instance = data['instance']
    model = joblib.load('model.pkl')
    prediction = model.predict([instance])[0]
    
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)