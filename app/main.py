from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f'ping {host}')
    subprocess.call(args, shell=False)

    return {'status': 'completed'}