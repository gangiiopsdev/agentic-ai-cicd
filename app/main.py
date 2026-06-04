from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() and '.' not in host:
        return {'status': 'error', 'output': 'Invalid host'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '--', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}