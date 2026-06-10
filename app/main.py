from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

allowed_hosts = ['google.com', 'example.com']

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', *shlex.split(host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}