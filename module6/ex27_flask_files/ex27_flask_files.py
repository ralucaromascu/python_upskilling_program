import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/scan")
def scan():
    dir_path = request.args['dirpath']
    if not os.path.isdir(dir_path):
        return f'The given directory is not a valid one.'
    else:
        files_list = []
        for (root, dirs, files) in os.walk(dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                files_list.append(pathfile)
        return str(files_list)
