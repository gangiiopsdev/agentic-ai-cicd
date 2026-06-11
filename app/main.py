from fastapi import FastAPI
import subprocess
import shlex

cmd = ['ping', shlex.quote(host)]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.call(cmd)
    return {'status': 'completed'}