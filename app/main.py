from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    return re.sub(r'[^a-zA-Z0-9.-]', '', host)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}