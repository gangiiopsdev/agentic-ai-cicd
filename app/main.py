from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    # Add logic to check if the host is safe (e.g., whitelist)
    allowed_hosts = ['safehost1.com', 'safehost2.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}