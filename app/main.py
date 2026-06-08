from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.split to avoid shell injection
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}'))
    return {'status': 'completed'}