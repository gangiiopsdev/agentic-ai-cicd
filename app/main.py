from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid input')
    return 'ping ' + host

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    command = safe_ping(host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}