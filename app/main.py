from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it is a valid hostname
    if not host.isalnum() or '.' not in host:
        return {'error': 'Invalid hostname'}
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}