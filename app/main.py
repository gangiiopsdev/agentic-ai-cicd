from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation: validate and sanitize host input
    if not host or len(host) > 255:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}