from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str) -> dict:
    try:
        # Validate the host input before using it in the command
        if not host.isalnum():
            raise ValueError('Invalid input')
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping_endpoint(host: Optional[str] = None) -> dict:
    if host is not None and host.isalnum():  # Basic validation to prevent shell injection
        return ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid input'}