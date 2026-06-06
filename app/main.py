from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}