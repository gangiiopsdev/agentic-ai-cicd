from fastapi import FastAPI
import subprocess
import shlex
def safe_host(host):
    return host.isdigit()
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not safe_host(host):
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e.stderr}'}
# Additional preventive controls
import os
os.environ['PATH'] = '/usr/bin:/bin'  # Restricting the PATH to prevent execution of arbitrary commands