from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    # Validate the host input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'success', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}