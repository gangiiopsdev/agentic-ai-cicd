from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_safe_host(host):
    # Enhanced regex to validate the host input more strictly
    return re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', str(1), host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}