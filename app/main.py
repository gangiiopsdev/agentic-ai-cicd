from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}