from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if host.strip() == '':
        return {"status": "failed", "message": "Host is empty"}
    subprocess.call(shlex.split(f'ping {shlex.quote(host)}')))
    return {"status": "completed"}