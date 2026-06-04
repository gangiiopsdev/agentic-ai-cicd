from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid host"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args, shell=False)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts