from fastapi import FastAPI
import subprocess
import os
def sanitize_input(value):
    if '/' in value or '..' in value or value.startswith('.'):
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):