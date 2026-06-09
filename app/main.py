from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host: str):
    allowed_hosts = {"example.com", "localhost"}
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}