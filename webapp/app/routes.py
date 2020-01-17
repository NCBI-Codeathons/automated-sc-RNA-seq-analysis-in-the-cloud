import os

from flask import (
    Blueprint, flash, request, redirect, render_template, current_app,
    url_for)
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

        # TODO: Generate unique ID
        id = generate_uniq_id()

        # TODO: Make a destination dir at {current_app.config['UPLOAD_FOLDER']}/{id}
        dest_dir = 'TODO!'

        for (name, file) in request.files.items():
            print(name, file)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    dest_dir,
                    filename
                ))
                # TODO:
                # flash(f'uploaded {name}')
            # TODO:
            # else:
            # 	flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        return redirect(url_for('start_processing', id), code=307)
        # HTTP 307 tells the browser to preserve POST,
        # rather than changing to a GET.


@blueprint.route('/start-processing/<id>', methods=['POST'])
def start_processing(id):
    # TODO: Start processing!
    start_processing(current_app.config['UPLOAD_FOLDER'], id)
    return redirect(please_wait('wait_processing', id))


@blueprint.route('/wait-processing/<id>',)
def wait_processing(id):
    # TODO!
    if output_exists_for_id(id):
        return redirect(url_for('done_processing', id))
    else:
        return render_template('wait-processing.html')
        # Put either a meta refresh or a javascript refresh on this page,
        # so it will retry every 5 seconds or so.

@blueprint.route('/done-processing/<id>',)
def done(id):
    # TODO!
    summary = create_summary(id)
    return render_template('done-processing.html', summary=summary)
