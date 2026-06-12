from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip():
        return False
    if '/' in host:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host parameter'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}