import hashlib
import os
import pickle
import time

from flask import Flask, request, jsonify, abort


def get_sha1(pathfile):
    chunk_size = 2048
    md = hashlib.sha1()
    with open(pathfile, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            md.update(chunk)
        file_hashed_sha1 = md.hexdigest()
    return file_hashed_sha1


class FileInfo:
    def __init__(self, filename, mtime, sha1):
        self.filename = filename
        self.mtime = mtime
        self.sha1 = sha1

    def __str__(self):
        return f'FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}'

    def __eq__(self, other):
        return type(other) == type(self) and self.filename == other.filename


class FileList:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.all_file_infos = []
        self.last_timestamp = 0


app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(412)
def precondition_failed(e):
    return jsonify(error=str(e)), 412


@app.route("/scan")
def scan():
    dir_path = request.args['dirpath']
    if not os.path.isdir(dir_path):
        abort(404, description='Directory not found')
    else:
        fl = FileList(dir_path)
        for (root, dirs, files) in os.walk(dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                fl.all_file_infos.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))
        fl.last_timestamp = time.time()
        with open(dir_path.replace('/', '-'), "wb") as f:
            pickle.dump(fl, f)
        return jsonify('File scanned successfully')


@app.route("/rescan")
def rescan():
    dir_path = request.args['dirpath']
    if not os.path.isdir(dir_path):
        abort(404, description='Directory not found')
    else:
        is_scanned = False
        pickle_name_dir = dir_path.replace('/', '-')
        new_fl = FileList(dir_path)
        for (root, dirs, files) in os.walk(dir_path, topdown=True):
            for file in files:
                pathfile = os.path.join(root, file)
                file_info = os.stat(pathfile)
                if file == pickle_name_dir:
                    is_scanned = True
                else:
                    new_fl.all_file_infos.append(FileInfo(file, file_info.st_mtime, get_sha1(pathfile)))
        new_fl.last_timestamp = time.time()
        if not is_scanned:
            abort(412, description='Directory not scanned before')
        else:
            with open(pickle_name_dir, "rb") as f:
                fl = pickle.load(f)

            update_dict = {'added': [], 'removed': [], 'changed': []}
# e
            for file_obj in new_fl.all_file_infos:
                if file_obj not in fl.all_file_infos:
                    update_dict['added'].append(getattr(file_obj, 'filename'))
            for file_obj in fl.all_file_infos:
                if file_obj not in new_fl.all_file_infos:
                    update_dict['removed'].append(getattr(file_obj, 'filename'))
            for file_obj1 in new_fl.all_file_infos:
                for file_obj2 in fl.all_file_infos:
                    if file_obj1 == file_obj2 and getattr(file_obj1, 'sha1') != getattr(file_obj2, 'sha1'):
                        update_dict['changed'].append(getattr(file_obj1, 'filename'))
            with open(dir_path.replace('/', '-'), "wb") as f:
                pickle.dump(new_fl, f)

            return jsonify(update_dict)
