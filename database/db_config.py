import os

basedir = os.path.abspath(os.path.dirname(__file__))
HOST = str(os.environ.get("DB_HOST"))
CLUSTER = str(os.environ.get("DB_CLUSTER"))
USERNAME = str(os.environ.get("DB_USERNAME"))
PASSWORD = str(os.environ.get("DB_PASSWORD"))

MONGODB_URI = 'mongodb+srv://' + USERNAME + ':' + PASSWORD + '@'+ CLUSTER + '.' + HOST + '/?retryWrites=true&w=majority'