from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ["example.com", "test.com"]
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}