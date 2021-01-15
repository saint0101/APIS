#!/usr/bin/env python3.7
# -*- encoding: utf-8 -*-

"""
    Test API fastapi
    install:
        - pip install fastapi
        - pip install uvicorn[standard]
"""
import uvicorn

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


if __name__ == '__main__':
    uvicorn.run("security:app")