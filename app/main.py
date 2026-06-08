from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    validate_host(host)
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}