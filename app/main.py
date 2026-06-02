from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 255

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid input'}
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}