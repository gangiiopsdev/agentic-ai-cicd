from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']  # Define allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)