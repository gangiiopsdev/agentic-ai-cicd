from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> bool:
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid input'}, 400
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}