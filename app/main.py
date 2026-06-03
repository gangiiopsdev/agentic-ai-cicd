from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or not all(c.isalnum() for c in host):
        raise ValueError("Invalid host")

    # Use shlex to safely handle the command arguments
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}