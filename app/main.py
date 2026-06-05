from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # More comprehensive validation of the 'host' parameter
    if not (host.isalnum() or host.replace('.', '', 1).isnumeric()) and '.' in host:
        raise ValueError('Invalid host format')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}