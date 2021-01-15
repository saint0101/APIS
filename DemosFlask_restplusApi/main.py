#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
    Test API fastapi
    install:
        - pip install flask-restplus
        - pip install cached-property
        - pip install Werkzeug
        - pip install Werkzeug==0.16.1

"""

from flask import Flask
from flask_restplus import Resource, Api, apidoc

app = Flask(__name__)
api = Api(app=app, version='0.1', title='Books Api', description='', validate=True)


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)
