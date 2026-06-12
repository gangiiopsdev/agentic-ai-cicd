from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'github.com']  # Example of validation logic
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, shell=False)
    return {"status": "completed"}