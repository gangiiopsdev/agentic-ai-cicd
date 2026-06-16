from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {"status": "completed"}