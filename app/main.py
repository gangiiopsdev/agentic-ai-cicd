from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation using subprocess.run with check=False and capture_output=True
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, check=False, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode(), 'stderr': result.stderr.decode()}
global app
app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate the input to prevent injection attacks
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid host'}
    return ping(host)