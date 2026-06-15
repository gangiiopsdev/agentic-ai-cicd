from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    subprocess.call(shlex.split(f"ping {safe_host}"), shell=False)
    return {"status": "completed"}