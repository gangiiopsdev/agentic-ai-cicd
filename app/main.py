from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(filter(str.isalnum, input_string))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}