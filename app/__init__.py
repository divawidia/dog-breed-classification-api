# memasukan liibrary yang diperlukan
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import os

app = Flask(__name__)

SWAGGER_URL = '/api/v1/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = str(os.environ.get("APP_URL"))+'/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Dog Breed Classifier API"
    },
)

app.register_blueprint(swaggerui_blueprint)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

from app import routes

#kembali ke halaman awal
if __name__ == "__main__":
    app.run()