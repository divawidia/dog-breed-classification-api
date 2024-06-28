# memasukan liibrary yang diperlukan
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
import os

app = Flask(__name__)

SWAGGER_URL = '/api/v1/docs'  # URL for exposing Swagger UI (without trailing '/')
# API_URL = 'http://127.0.0.1:5000/swagger.json'  # Our API url (can of course be a local resource)
API_URL = 'https://dog-breed-classifier-api-7zz24sawna-et.a.run.app/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Dog Breed Classifier API"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

from app import routes

#kembali ke halaman awal
if __name__ == "__main__":
    app.run()