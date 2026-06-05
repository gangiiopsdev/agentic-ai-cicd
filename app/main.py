from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement a whitelist or regex to allow only safe hosts
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    sanitize_host(host)
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}