from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_str):
    if not input_str.isalnum():
        raise ValueError('Invalid input')
    return input_str

@app.get('/ping')
def ping(host: str):  # host: str
    host = sanitize_input(host)
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise Exception('Ping failed')
    return {'status': 'completed'}