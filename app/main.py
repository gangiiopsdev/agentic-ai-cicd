from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent injection
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host'}

    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, text=True)

    return {'status': 'completed'}