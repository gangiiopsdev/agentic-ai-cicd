from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using list instead of shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}

def is_safe_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts