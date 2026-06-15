from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_host(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)