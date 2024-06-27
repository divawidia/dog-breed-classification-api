from pymongo import MongoClient
import db_config
import pandas as pd

client = MongoClient(db_config.MONGODB_URI)

def seed_dog_breed():
    database = client['dogBreedClassifier']
    collection = database['dogBreeds']
    data1 = pd.json_normalize(collection.find())
    data2 = pd.read_csv('database/akc-data-latest-translated.csv')

    if len(data1) == len(data2):
        print('Dog Breed data has been seeded')
    else:
        data2 = data2.to_dict('records')
        collection.insert_many(data2)
        print('Dog Breed data successfully seeded into database')

def seed_breed_label():
    database = client['dogBreedClassifier']
    collection = database['dogLabels']

    data1 = pd.json_normalize(collection.find())
    data2 = pd.read_csv('database/dog_labels.csv')

    if len(data1) == len(data2):
        print('Dog Label data has been seeded')
    else: 
        data2 = data2.to_dict('records')
        collection.insert_many(data2)
        print('Dog Label data successfully seeded into database')

if __name__ == "__main__":
    seed_dog_breed()
    seed_breed_label()