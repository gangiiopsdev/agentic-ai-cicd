from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation without using shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):  # Add validation for the host parameter
        ping_safe(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation, adjust as needed
    return host.strip().replace('.', '').isalnum()