from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isdigit() and len(host) == 4:
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host address')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}