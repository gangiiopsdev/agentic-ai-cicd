from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "denied", "reason": "Invalid host"}