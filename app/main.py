from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    # Validate and sanitize the input before using it in the subprocess call
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(args)

def validate_host(host):
    allowed_hosts = ['192.168.1.1', '10.0.0.1']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}