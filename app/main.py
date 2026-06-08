from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Using subprocess.run with shell=False for a safer approach
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's safe to use with subprocess
    if not host.isalnum() or '.' in host:
        return {'status': 'invalid', 'message': 'Invalid host'}
    return safe_ping(host)