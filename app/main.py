from fastapi import FastAPI
import subprocess

app = FastAPI()

def _ping(host: str):
    # Secure implementation using `subprocess.run` without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Basic validation of the host input
        return {'status': 'error', 'message': 'Invalid hostname'}
    return _ping(host)