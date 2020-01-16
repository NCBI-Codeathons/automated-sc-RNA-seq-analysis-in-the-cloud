from flask import Flask

UPLOAD_FOLDER = '/Users/sanjanashah/Desktop/tms_test'
app = Flask(__name__)

from app import routes2
#from app import routes


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



