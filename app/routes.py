# memasukan library yang dibutuhkan dalam route
from flask import request, jsonify

import json
import os
from app import app
from app.controller import PredictController

api_prefix = '/api/v1/'

# route home
@app.route("/")
def helloWorld():
  return "Hello, this app is working!"

@app.route(api_prefix + 'predict', methods=['POST'])
def predict():
  return PredictController.post_predict_image()