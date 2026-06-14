from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}