from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}