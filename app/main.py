from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host):
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping'] + shlex.split(escaped_host)
    subprocess.call(args, shell=False)
    return {"status": "completed"}