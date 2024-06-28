# memasukan liibrary yang diperlukan
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
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
)

app.register_blueprint(swaggerui_blueprint)

from app import routes

#kembali ke halaman awal
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8090)))
    app.run()