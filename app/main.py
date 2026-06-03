from fastapi import FastAPI
import subprocess
import shlex
import re
import os

app = FastAPI()

def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Use subprocess.run instead of os.popen for better security
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)