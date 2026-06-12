from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}