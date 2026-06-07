from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '--no-host-alias', '--non-privileged', host], check=True)
    return {'status': 'completed'}