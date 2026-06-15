from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.strip().isalnum():
        raise ValueError("Invalid host")
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}