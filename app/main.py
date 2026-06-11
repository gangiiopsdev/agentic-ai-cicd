from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_and_sanitize_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}

def validate_and_sanitize_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    sanitized_host = subprocess.run(['echo', host], capture_output=True, text=True).stdout.strip()
    return sanitized_host in allowed_hosts