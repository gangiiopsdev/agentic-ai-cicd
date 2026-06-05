from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.strip() or any(c in host for c in '<>"/\|&*?{}[]`'):  # Simple validation example
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}