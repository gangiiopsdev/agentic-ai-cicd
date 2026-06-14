from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'localhost']
def safe_ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        # Use shlex.quote to safely quote the command arguments
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Add input validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)