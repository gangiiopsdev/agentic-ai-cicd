from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', '-c', '1', host], check=True)  # Use parameterized ping with a count to avoid shell interpretation and ensure safe execution
    return {'status': 'completed'}