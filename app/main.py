from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure host input is sanitized and validated
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}