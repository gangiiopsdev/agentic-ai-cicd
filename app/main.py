from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 50

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}