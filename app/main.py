from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    args = ['ping', host]
    subprocess.call(args)
app = FastAPI()
@app.get('/ping')
def ping_safe(host: str):
    return safe_ping(host)