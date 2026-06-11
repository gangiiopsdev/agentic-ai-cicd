from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(hostname):
    # Define a list of safe hosts or perform additional checks
    safe_hosts = ['127.0.0.1', '::1']
    return hostname in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    subprocess.call(["ping", host])
    return {"status": "completed"}