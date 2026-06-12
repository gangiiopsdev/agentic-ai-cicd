from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
@app.get("/ping")
def ping(host: str):
    args = shlex.split(f"ping {host}")
    # Validate host to ensure it's a safe input
    if not is_safe_host(host):
        return {"error": "Invalid host"}, 400
    subprocess.call(args)
    return {"status": "completed"}
def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hosts
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts