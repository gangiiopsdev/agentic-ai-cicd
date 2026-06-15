from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', '127.0.0.1']
    if host in allowed_hosts:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)