from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    return subprocess.call(args)

def validate_host(host):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}