from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}