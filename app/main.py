from fastapi import FastAPI
import subprocess
import re
global safe_hosts = ['localhost', '127.0.0.1'] # Restrict hosts to known safe ones
app = FastAPI()
def ping(host: str):
    if host.strip() not in safe_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
global ping_func = app.get('/ping')(ping)