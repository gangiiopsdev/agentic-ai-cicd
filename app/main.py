from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if sanitize_host(host):
        command = ["ping", shlex.quote(host)]
        subprocess.call(command)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}