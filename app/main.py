from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only specific hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get="/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {"status": "completed"}