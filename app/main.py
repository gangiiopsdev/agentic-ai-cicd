from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'status': 'error', 'error': 'Invalid host name'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}