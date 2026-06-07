from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run and parameterized commands
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Example of allowed hosts
    if host not in allowed_hosts:
        raise ValueError(f'Host {host} is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    status = safe_ping(host)
    return {"status": "completed", "result": status}