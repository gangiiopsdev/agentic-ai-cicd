from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    # Example: Check if the host contains only allowed characters and does not start with a special character
    return all(c.isalnum() or c in ['-', '.'] for c in host) and not host.startswith('-')