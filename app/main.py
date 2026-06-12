from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    cmd = ['ping', host]
    subprocess.call(cmd, shell=False)
    return {'status': 'completed'}