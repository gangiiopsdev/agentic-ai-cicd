from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}