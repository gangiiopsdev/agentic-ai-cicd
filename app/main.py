from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or ':' in host:
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

# Preventive Controls:
# 1. Validate and sanitize the input for host.
# 2. Use a whitelist of allowed hosts or networks.