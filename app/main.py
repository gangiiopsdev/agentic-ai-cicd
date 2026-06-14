from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    args = ['ping', '-c 1', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}