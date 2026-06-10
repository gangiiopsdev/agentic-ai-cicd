from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid host input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}