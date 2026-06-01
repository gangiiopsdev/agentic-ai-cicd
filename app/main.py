from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Fixed implementation using a list instead of shell=True
    subprocess.call(['ping', host])
    return {'status': 'completed'}