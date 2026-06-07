from fastapi import FastAPI
import subprocess
import shlex
def is_safe_host(host):
    # Define a list of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail="Host is not allowed")
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}