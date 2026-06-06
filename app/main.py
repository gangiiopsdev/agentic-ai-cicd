from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):

    if validate_host(host):
        subprocess.call(f"ping {host}", shell=True)
    else:
        raise Exception("Invalid host")

    return {"status": "completed"}