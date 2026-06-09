from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Implement logic to validate and sanitize host input
    return host.strip() in ['localhost', '127.0.0.1']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}