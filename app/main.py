from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True, shell=False)

@app.get('/ping')
def ping_safe(host: str):
    # Validate input
    if not host or not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    ping(host)
    return {'status': 'completed'}