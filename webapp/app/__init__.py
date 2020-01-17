from flask import Flask

# TODO: Change upload folder!
UPLOAD_FOLDER = '../'
app = Flask(__name__)

from app import routes

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
# TODO: app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
