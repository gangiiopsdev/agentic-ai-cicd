from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return ping(host)