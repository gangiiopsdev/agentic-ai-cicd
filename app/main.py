from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with arguments tuple
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize the host parameter
    if not host or len(host) > 255 or not all(c.isalnum() for c in host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)