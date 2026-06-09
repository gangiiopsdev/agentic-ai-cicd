from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError('Invalid input')
    args = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(args)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)