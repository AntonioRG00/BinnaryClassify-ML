import pickle
from flask import Flask, request, jsonify
import json
import numpy as np

app = Flask("FlaskApi")

with open('../model/churn-model.pkl', 'rb') as f:
    dv, model = pickle.load(f)

def predict_single(data):
    data = dv.transform([data])
    return model.predict(data)[0]

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = predict_single(data)
    return json.dumps(prediction, cls=NpEncoder)

if __name__ == '__main__':
    app.run(debug=True, port=8000)