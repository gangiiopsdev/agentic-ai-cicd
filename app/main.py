from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.strip() or not all(c.isalnum() for c in host):
        raise ValueError('Invalid host parameter')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping'] + shlex.split(host)
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}