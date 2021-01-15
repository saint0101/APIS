#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
    Test API fastapi
    install:
        - pip install Flask-API
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
