from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def ping(host: str) -> Dict[str, str]:
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str) -> Dict[str, str]:
    # Validate the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)