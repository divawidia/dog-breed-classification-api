# memasukan liibrary yang diperlukan
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)

SWAGGER_URL = '/api/v1/docs'  # URL for exposing Swagger UI (without trailing '/')

# API_URL = 'http://127.0.0.1:5000/swagger.json'  # Our API url (can of course be a local resource)
API_URL = 'https://teman-ngorte-api-jum5dt3leq-et.a.run.app/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Teman Ngorte API"
    },
)

app.register_blueprint(swaggerui_blueprint)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.model import dog_breed
from app import routes

#kembali ke halaman awal
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8090)))
    app.run()