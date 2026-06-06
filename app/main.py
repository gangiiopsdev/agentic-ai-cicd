from fastapi import FastAPI
import shlex
import os

app = FastAPI()

def is_valid_host(host):
    return all(c.isalnum() or c in '-.' for c in host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}