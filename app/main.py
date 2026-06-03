from fastapi import FastAPI
import subprocess
import os
def ping(host: str):
    # Safer implementation using subprocess.run with validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if not os.path.exists('ping'):
        return {'status': 'error', 'message': 'Executable not found'}
    return ping(host)