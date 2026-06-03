from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add logic to validate and sanitize host input
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    # Safe implementation
    subprocess.call(['ping', host])
    return {"status": "completed"}