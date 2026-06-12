from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def ping(host: str) -> Dict:
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str) -> Dict:
    # Validate and sanitize the host input
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)