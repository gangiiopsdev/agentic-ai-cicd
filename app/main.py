from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    if not host or len(host) > 256:
        raise ValueError("Invalid host parameter")
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    # Use subprocess.Popen for better control
    process = subprocess.Popen(shlex.split(f'ping {host}'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return {'status': 'completed', 'stdout': stdout.decode('utf-8'), 'stderr': stderr.decode('utf-8')}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)