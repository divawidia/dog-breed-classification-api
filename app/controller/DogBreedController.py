import urllib
import urllib.parse
from flask import request
from app import response
from database import db_config
from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads

client = MongoClient(db_config.MONGODB_URI)
database = client['dogBreedClassifier']
collection = database['dogBreeds']

def get_breed_data():
    dog_breed = request.args.get('breed')
    dog_breed = urllib.parse.unquote(dog_breed)
    try:
        data = loads(dumps(collection.find_one({'breed': dog_breed}, projection = {"_id": False})))
        return response.success(values=data, message="Success")
    except Exception as e:
        return response.badRequest(values=[], message=e)