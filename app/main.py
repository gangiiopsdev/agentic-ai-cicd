from fastapi import FastAPI
import subprocess
cimport subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    # Use a whitelist of allowed hosts or validate the input more strictly
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)