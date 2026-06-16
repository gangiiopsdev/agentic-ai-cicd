from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host or len(host) > 256:
        raise ValueError("Invalid host parameter")
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(["ping", "/bin/ping", host], shell=False)
    return {"status": "completed"}