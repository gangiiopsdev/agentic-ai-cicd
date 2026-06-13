from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate input to prevent command injection
    if host.strip() != host or any(char in host for char in ' ;&|<>`$'):  # Basic validation
        raise ValueError('Invalid host name')
    return subprocess.call(['ping', '-c', '1', host], shell=False)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed'}