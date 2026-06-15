from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Add logic to validate the hostname for safety
    return all(c.isalnum() or c in '._-' for c in hostname)

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "failed", "error": "Invalid hostname"}
    subprocess.call(['ping', host])
    return {"status": "completed"}