from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping_secure(host: str):
    # Validate and sanitize input
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}