from fastapi import FastAPI
import subprocess
def safe_ping(host):
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    if safe_host == host:
        raise ValueError("Invalid characters in hostname")
    return subprocess.call(['ping', safe_host])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}