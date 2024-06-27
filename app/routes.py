from app import app
from app.controller import PredictController, DogBreedController

api_prefix = '/api/v1/'

# route home
@app.route("/")
def helloWorld():
  return "Hello, this app is working!"

@app.route(api_prefix + 'predict', methods=['POST'])
def predict():
  return PredictController.post_predict_image()

@app.route(api_prefix + 'dogs', methods=['GET'])
def dog_breed():
  return DogBreedController.get_breed_data()