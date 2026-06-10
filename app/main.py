from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    command = ['ping', *shlex.split(host)]
    if not all(os.path.basename(p) in ['ping'] for p in command):
        return {'status': 'error', 'message': 'Invalid command'}
    subprocess.run(command, check=True)
    return {'status': 'completed'}