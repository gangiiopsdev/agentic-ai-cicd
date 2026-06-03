from fastapi import FastAPI
import subprocess
import os
def sanitize_input(value):
    if '/' in value or '..' in value or value.startswith('.'):
        return False
    return True

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'status': 'error', 'output': 'Host is required'}
    if not sanitize_input(host):
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(['ping', os.path.abspath(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}