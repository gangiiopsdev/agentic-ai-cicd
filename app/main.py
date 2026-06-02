from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}