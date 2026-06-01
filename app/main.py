from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None or not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host format'}
    return safe_ping(host)