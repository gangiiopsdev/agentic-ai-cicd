from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(shlex.split(f'ping {host}'))

def is_safe_host(host: str):
    # Implement logic to validate the host, e.g., allow only specific domains or IP addresses
    return True

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}