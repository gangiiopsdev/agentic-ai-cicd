from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate the host to ensure it's a trusted IP or domain
    if is_trusted_host(host):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Untrusted host")

def is_trusted_host(host):
    # Implement your validation logic here
    return True

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}