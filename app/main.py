from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    safe_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return safe_host

@app.get('/ping')
def ping(host: str):
    # Sanitize host input
    safe_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}