from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = shlex.split(f'ping {host}')
        subprocess.run(args)
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}