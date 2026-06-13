from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in [".", "/"] for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host name"}
    command = shlex.split(f'ping {host}')
    subprocess.call(command)
    return {"status": "completed"}