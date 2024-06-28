from app import app
from app.controller import PredictController, DogBreedController
from flask_cors import cross_origin
from flask import jsonify
import json


api_prefix = '/api/v1/'

# route home
@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, this app is working!"

@app.route(api_prefix + 'predict', methods=['POST'])
def predict():
  return PredictController.post_predict_image()

@app.route(api_prefix + 'dogs', methods=['GET'])
def dog_breed():
  return DogBreedController.get_breed_data()

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))