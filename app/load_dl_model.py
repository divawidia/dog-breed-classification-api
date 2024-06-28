from tensorflow import keras 
import pandas as pd

# mengambil data label nama ras anjing
dog_names = pd.read_csv('database/dog_labels.csv')
dog_names = dog_names['0'].tolist()

finetuned_Resnet50_model = keras.models.load_model('saved_models/weights.best.hdf5')

# mendefinisikan model resnet50
ResNet50_model = keras.applications.ResNet50(weights='imagenet')