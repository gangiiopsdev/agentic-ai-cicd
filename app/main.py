from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host.strip().lower() in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not safe_host(host):
        return {"error": "Invalid host"}
    subprocess.call(['ping', quote(host)])
    return {"status": "completed"}