from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Validate and sanitize the host input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'output': 'Invalid host input'}