from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input using a whitelist of allowed hosts or use a regex pattern
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input using a whitelist of allowed hosts or use a regex pattern
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        return safe_ping(host)
    else:
        return {'error': 'Invalid host'}