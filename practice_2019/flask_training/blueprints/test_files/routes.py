import os
from flask import Blueprint, request
from werkzeug.utils import secure_filename

files_bp = Blueprint('files_bp', __name__, template_folder='templates')


@files_bp.route('/file_from_server/<path:val>') # http://127.0.0.1:5000/file_from_server/test_files/files/test1.txt
def file_test_from_server(val):
    with open(val) as f:
        return f.read()

@files_bp.route('/file_from_ui', methods=['POST'] )
def file_upload():
    file = request.files['file']
    file_path = os.path.join('blueprints/test_files/files', secure_filename(file.filename))
    file.save(file_path)

    with open(file_path) as f:
        return f.read()


