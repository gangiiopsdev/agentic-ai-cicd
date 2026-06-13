from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.startswith('127.0.0.1') or host.startswith('::1'):  # Allow only local hosts
        subprocess.call(['ping', host])
    else:
        raise ValueError('Ping requests to non-local hosts are not allowed.')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}