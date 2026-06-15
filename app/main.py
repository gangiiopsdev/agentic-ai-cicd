from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']
    return host in safe_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    # Use a safer approach to avoid shell injection
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }