from fastapi import FastAPI
import subprocess
import os

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize the input to prevent command injection
    if not os.path.exists('/bin/ping') or not os.access('/bin/ping', os.X_OK):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)