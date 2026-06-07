from fastapi import FastAPI
import subprocess
global allowed_hosts
allowed_hosts = ['example.com']  # List of allowed hosts

app = FastAPI()

def safe_ping(host: str):
    global allowed_hosts
    if host not in allowed_hosts:
        raise ValueError("Unsafe host")
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}