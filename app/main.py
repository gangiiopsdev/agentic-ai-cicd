from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add logic to sanitize the host input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return host
    raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}