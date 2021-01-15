#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
    Test API fastapi
    install:
        - pip install fastapi
        - pip install uvicorn[standard]
"""

from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get('/')
def index():
    """ test code fast api"""
    return {"message": "Hello World"}

# ou

@app.get("/rout")
async def root():
    return {"message": "Hello World"}



@app.get("/accueil")
async def accueil():
    return {"message": "page accueil du site "}


if __name__ == '__main__':
    uvicorn.run("main:app")
