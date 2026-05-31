from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        command = ['ping', shlex.quote(host)]
        subprocess.call(command)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}