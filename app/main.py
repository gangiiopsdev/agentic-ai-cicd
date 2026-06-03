from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum() or '.' in host:
        return {'status': 'invalid input'}
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}