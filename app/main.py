from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add validation logic here to ensure host is a trusted IP or hostname
    return True

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}