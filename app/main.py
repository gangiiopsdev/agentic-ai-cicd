from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}