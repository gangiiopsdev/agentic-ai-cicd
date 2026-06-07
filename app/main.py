from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: Optional[str] = None):
    if host is None or len(host) == 0:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    validated_host = validate_host(host)
    if not validated_host:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(validated_host)

def validate_host(host: str) -> Optional[str]:
    # Add logic to validate the host input, e.g., check for allowed characters or format.
    if host.isalnum():
        return host
    return None