import os

from flask import Flask

from . import routes2


def create_app(test_config=None):
    # TODO: Change upload folder!
    UPLOAD_FOLDER = '/tmp'
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = "secret key"
    # TODO: app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    app.register_blueprint(routes2.blueprint)

    return app
