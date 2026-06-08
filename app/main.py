from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate host input to ensure it's safe
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

def is_safe_host(host):
    # Implement validation logic here (e.g., whitelist of allowed hosts)
    allowed_hosts = {'example.com', 'test.example.com'}
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}