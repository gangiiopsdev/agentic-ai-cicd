from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'error': 'Invalid input'}, 400
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}