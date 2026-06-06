from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return host and host.isalnum() and '.' in host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', '-c', str(4), safe_host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}
    return {'status': 'completed', 'output': result.stdout}