from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add allowed hosts here
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {
            "status": "completed",
            "output": result.stdout
        }
    else:
        return {"error": "Invalid host"}, 403