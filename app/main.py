from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    # Use a safe and explicit command to avoid execution of untrusted input
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}