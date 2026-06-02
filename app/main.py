from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid input')
app = FastAPI()
@app.get('/ping')
def ping(host: str):