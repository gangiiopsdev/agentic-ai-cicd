from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['google.com', 'example.com']
    return host in allowed_hosts

def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {"status": "completed"}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)