from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Add validation logic here
    allowed_hosts = ['example.com', '192.168.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}