from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '.' not in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)