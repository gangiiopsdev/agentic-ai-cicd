from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.com"]  # Define a list of allowed hosts
    return host in allowed_hosts