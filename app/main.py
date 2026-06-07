from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.strip() and not any(char in host for char in [';', '&', '|', '$']):  # Basic input validation
        subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}