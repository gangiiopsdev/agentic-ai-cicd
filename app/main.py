from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() and all(c.isalnum() or c in ('.', '-') for c in host):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}