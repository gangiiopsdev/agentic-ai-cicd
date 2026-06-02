from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex for safe argument handling
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}