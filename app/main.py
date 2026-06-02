from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout.decode().strip()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)