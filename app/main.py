from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if all(c.isalnum() or c in ('.', '-', '_') for c in host) and len(host) <= 255:
        subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}