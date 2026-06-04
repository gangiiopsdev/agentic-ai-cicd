from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add allowed hosts here
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Unsafe host")

    return {"status": "completed"}