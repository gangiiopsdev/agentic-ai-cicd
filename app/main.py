from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex
    command = f'ping {shlex.quote(host)}'
    subprocess.run(command, shell=False)
    return {'status': 'completed'}