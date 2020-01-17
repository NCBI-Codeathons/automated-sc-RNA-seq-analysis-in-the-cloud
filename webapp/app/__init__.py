from app import routes2
from flask import Flask

# change upload folder
UPLOAD_FOLDER = '../'
app = Flask(__name__)

#from app import routes


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
