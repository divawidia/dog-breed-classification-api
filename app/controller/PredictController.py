from tensorflow import keras 
import numpy as np
import os
from flask import request
from app.load_dl_model import dog_names, finetuned_Resnet50_model, ResNet50_model
from app import response

def path_to_tensor(img_path):
    # memuat gambar rgb sebagai PIL.Image.Image type
    img = keras.utils.load_img(img_path, target_size=(224, 224))
    
    # koversi PIL.Image.Image type menjadi 3D tensor dengan bentuk (224, 224, 3)
    x = keras.utils.img_to_array(img)
    
    # konversi 3D tensor ke 4D tensor dengan bentuk (1, 224, 224, 3) dan mereturnkan 4D tensor
    return np.expand_dims(x, axis=0)

def ResNet50_predict_labels(img_path):
    # menghasilkan nilai predksi vektor untuk foto pada img_path
    img = keras.applications.resnet.preprocess_input(path_to_tensor(img_path))
    return np.argmax(ResNet50_model.predict(img))

# returns "True" jika anjing terdeteksi pada gambar
def dog_detector(img_path):
    prediction = ResNet50_predict_labels(img_path)
    return ((prediction <= 268) & (prediction >= 151))

def Resnet50_predict_breed(img_path):
    # extract bottleneck features
    bottleneck_feature = keras.applications.ResNet50(weights='imagenet', include_top=False).predict(keras.applications.resnet.preprocess_input(path_to_tensor(img_path)))
    
    # obtain predicted vector
    predicted_vector = finetuned_Resnet50_model.predict(bottleneck_feature)
    
    # return dog breed that is predicted by the model
    dog_breed = dog_names[np.argmax(predicted_vector)]
    confidence_value = round(predicted_vector[0][np.argmax(predicted_vector)]*100,2)
    
    return dog_breed, confidence_value

def api_predict_response(dog_breed, confidence, message):
    resp = {}
    resp["dog_breed"] = dog_breed
    resp["confidence"] = f"{confidence} %"
    resp["response_message"] = message
    return resp

def breed_detector(img_path):
    prediction_result = Resnet50_predict_breed(img_path)
    dog_breed = prediction_result[0]
    confidence_value = prediction_result[1]
    # dog detector achieved the best accuracy
    if dog_detector(img_path):
        message = 'Aku tebak ini '+ str(confidence_value) + '% anjing ras '+ dog_breed
        return api_predict_response(dog_breed, confidence_value, message)
    else:
        message = 'Hmmm... sepertinya itu bukan foto anjing deh, coba kirim foto yang berisi anjing!'
        return api_predict_response(None, 0, message)

def post_predict_image():
    file = request.files.get('image')
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return response.badRequest(values=[], message="Image is required")
    try:
        tmp_file = f'temp_foto/{file.filename}'
        file.save(tmp_file)
        prediction = breed_detector(tmp_file)
        os.remove(tmp_file)
        return response.success(values=prediction, message="Success")
    except Exception as e:
        return response.badRequest(values=[], message=e)