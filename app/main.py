from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

allowed_hosts = ['8.8.8.8', '127.0.0.1']

def validate_host(host):
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {
            "status": "failed",
            "message": "Invalid host"
        }

    # Use os.system instead of subprocess to avoid command injection
    full_command = f'ping {host}'
    os.system(full_command)

    return {
        "status": "completed"
    }