from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    return ping(host)

@app.get("/ping")
def ping_route(host: str):
    return safe_ping(host)

def validate_host(host: str):
    # Add validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts