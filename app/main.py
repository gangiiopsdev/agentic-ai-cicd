from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Sanitize and validate input more robustly
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    # Validate and sanitize input to prevent shell injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)