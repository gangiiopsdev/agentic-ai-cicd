from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    
    # Secure implementation using subprocess.run with shell=False and safe arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode == 0:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': 'Ping failed'}