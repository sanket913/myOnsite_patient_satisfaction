from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('trained_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    wait_time = data['wait_time']
    staff_friendliness = data['staff_friendliness']
    cleanliness = data['cleanliness']
    quality_of_care = data['quality_of_care']
    

    features = [[wait_time, staff_friendliness, cleanliness, quality_of_care]]
    
    prediction = model.predict(features)[0]
    
    return jsonify({'satisfaction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
