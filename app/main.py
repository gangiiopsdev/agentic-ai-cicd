from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True and proper validation of host
    if host.strip() and all(c.isalnum() or c in '-._' for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host name')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}