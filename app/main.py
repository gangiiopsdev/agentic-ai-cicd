from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
@app.get("/ping")
def ping(host: str):safe_ping(host)
parsed_host = shlex.quote(host)args = ["ping", parsed_host]subprocess.run(args, check=True)return {"status": "completed"}