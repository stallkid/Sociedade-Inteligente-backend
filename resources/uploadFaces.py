from flask import Flask, url_for, send_from_directory, request
from flask_restful import Resource
import logging, os
import json
import base64
from werkzeug import secure_filename


class UploadFacesResource(Resource):

    def create_new_folder(local_dir):
        newpath = local_dir
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        return newpath

    def post(self):
        data = request.get_json(force=True)
        with open(data["_parts"][0][1] + ".png", "wb") as fh:
            fh.write(base64.b64decode(data["_parts"][1][1]))
