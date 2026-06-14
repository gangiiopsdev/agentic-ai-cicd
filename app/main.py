from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "invalid_host"}
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True, shell=False)  # Ensure shell=False
    return {"status": "completed"}