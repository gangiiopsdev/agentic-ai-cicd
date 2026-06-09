from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'error', 'message': 'Invalid host input'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}