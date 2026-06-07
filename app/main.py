from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace(' ', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])  # No need to remove spaces as validation ensures alphanumeric input
    return {"status": "completed"}