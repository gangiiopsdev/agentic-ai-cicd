from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # Add safe hosts here
    return host in safe_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}