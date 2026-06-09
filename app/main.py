from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def run_ping(host: str):
    # Sanitize input to prevent command injection
    host = host.strip()
    if not re.match(r'^[a-zA-Z0-9]+$', host):  # Allow only alphanumeric characters
        return {'status': 'invalid'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)