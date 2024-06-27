from tensorflow import keras 
import numpy as np
import pandas as pd

# mengambil data label nama ras anjing
dog_names = pd.read_csv('dog_labels.csv')
dog_names = dog_names['0'].tolist()

finetuned_Resnet50_model = keras.models.load_model('saved_models/weights.best.hdf5')

# mendefinisikan model resnet50
ResNet50_model = keras.applications.ResNet50(weights='imagenet')

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
    response = []
    resp = {}
    resp["dog_breed"] = dog_breed
    resp["confidence"] = f"{confidence} %"
    resp["response_message"] = message
    response.append(resp)
    return response

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