from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping_secure(host: str):
    # Validate and sanitize the host input
    if not host or not host.strip():
        return {'status': 'error', 'output': 'Invalid host'}
    args = shlex.split(f'ping -c 1 {host}')
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}