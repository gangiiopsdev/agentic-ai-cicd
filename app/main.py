from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to ensure it is a valid hostname or IP address
    if not host.replace('.', '').isalnum():
        return {"status": "invalid_host"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)