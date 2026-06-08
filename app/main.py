from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(["ping", host])
    else:
        return {"status": "failed", "message": "Invalid host"}

    return {"status": "completed"}