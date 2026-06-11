from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host.isalnum() and '.' in host:
        result = subprocess.run(['ping', re.escape(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid input'}

# Additional security checks and validation
allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
if host not in allowed_hosts:
    return {'status': 'error', 'message': 'Unauthorized access attempt'}