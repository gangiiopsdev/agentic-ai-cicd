from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host or not host.isalnum():
        return {'error': 'Invalid input'}, 400
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}