import os

from flask import (
    Blueprint, flash, request, redirect, render_template, current_app)
from werkzeug.utils import secure_filename


blueprint = Blueprint('routes', __name__, template_folder='templates')


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'h5ad'])


# use pathlib instead
def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/')
def upload_form():
    return render_template('uploads.html')


@blueprint.route('/', methods=['POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        for (name, file) in request.files.items():
            print(name, file)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    current_app.config['UPLOAD_FOLDER'],
                    filename
                ))
                # TODO:
                # flash(f'uploaded {name}')
            # TODO:
            # else:
            # 	flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            # 	return redirect(request.url)
        return redirect('/')
