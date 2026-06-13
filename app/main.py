from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')

    # Sanitize input to prevent injection attacks
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)

    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}