from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate host input to ensure it's safe to ping
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return run_ping(host)