from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it's safe
    if not is_safe_host(host):
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}

def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only localhost or specific IP ranges
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts