import os

from app import app
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'h5ad'])


# use pathlib instead
def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('uploads.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part:
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        for (name, file) in request.files.items():
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # TODO
                # flash(f'uploaded {name}')
            # TODO
            # else:
            #   flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        return redirect('/')


if __name__ == "__main__":
    app.run()
