from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def escape_user_input(user_input):
    return ''.join(ch for ch in user_input if ch.isalnum() or ch in '.-')

@app.get('/ping')
def ping(host: str):
    host = escape_user_input(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}