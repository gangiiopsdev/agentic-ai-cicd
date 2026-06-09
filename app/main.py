from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent shell injection
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}
    else:
        return {'status': 'error', 'message': 'Invalid input'}