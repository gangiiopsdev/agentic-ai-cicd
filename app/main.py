from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.call(['ping', '-c', '1', host])  # Use parameterized ping with a count to avoid shell interpretation
    return {'status': 'completed'}