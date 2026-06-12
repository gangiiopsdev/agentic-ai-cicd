from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with explicit shell=False and validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}