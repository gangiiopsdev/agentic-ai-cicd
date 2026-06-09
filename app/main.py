from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Safe implementation
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in the subprocess call
    if not validate_and_sanitize_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}

def validate_and_sanitize_host(host: str) -> bool:
    # Implement validation and sanitization logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts