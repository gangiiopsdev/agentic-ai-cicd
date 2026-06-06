from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'localhost' in host or '127.0.0.1' in host:
        return subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host for ping operation')

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_ping(host)
    return {"status": "completed"}