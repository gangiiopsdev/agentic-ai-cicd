from fastapi import FastAPI
import subprocess
from shlex import quote
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']  # Replace with actual whitelist
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    result = subprocess.run(['ping', quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}