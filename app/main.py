from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/example")
def read_example():
    return {"message": "Hello, World!"}