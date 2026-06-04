from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        args = ['ping', host]
        subprocess.call(args, shell=False)
    else:
        raise ValueError('Invalid input for host')