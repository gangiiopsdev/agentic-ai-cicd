from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    cmd = ['ping', *shlex.split(host)]
    subprocess.call(cmd)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}