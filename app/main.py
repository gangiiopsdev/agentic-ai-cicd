from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and escaping
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}