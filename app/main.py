from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}
def is_safe_host(host):
    # Add logic to validate the host
    allowed_hosts = ['example.com']
    return host in allowed_hosts