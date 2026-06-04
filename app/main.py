from fastapi import FastAPI
import subprocess

cimport = __import__

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}