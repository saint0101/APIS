#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
    Test API fastapi
    install:
        - pip install Flask-API
"""

from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/')
def index():
    return {'message': 'index page flask-api'}


@app.route('/example/')
def example():
    return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True)