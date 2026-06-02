from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}