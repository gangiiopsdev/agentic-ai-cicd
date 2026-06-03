from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'message': 'Invalid host'}
    return host
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'error':
        return result
    subprocess.call(['ping', result])
    return {'status': 'completed'}