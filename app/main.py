from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_hostname(hostname):
    # Simple example of validation logic
    return hostname.isalnum() and '.' in hostname

@app.get("/ping")
def ping(host: str):
    if not is_safe_hostname(host):
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.call(["ping", host])
    return {"status": "completed"}