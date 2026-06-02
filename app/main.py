from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.isdigit():
        raise ValueError("Invalid host")

@app.get="/ping")
def ping(host: str):
    validate_host(host)
    cmd = ['ping'] + shlex.split(host)
    subprocess.run(cmd, check=True, capture_output=True)
    return {"status": "completed"}