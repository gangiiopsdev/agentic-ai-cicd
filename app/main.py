from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']
def safe_ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        # Use subprocess.run with shell=False to avoid command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Add input validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)