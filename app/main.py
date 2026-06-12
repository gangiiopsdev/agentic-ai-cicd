from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host:
        return {'error': 'Host cannot be empty'}
    # Use a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        return {'error': 'Unauthorized host'}
    # Use subprocess.run with list to avoid shell=True
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {
        'status': 'completed',
        'stdout': result.stdout,
        'stderr': result.stderr
    }

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)