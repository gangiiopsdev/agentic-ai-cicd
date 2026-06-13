from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize input before passing it to subprocess
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed'}