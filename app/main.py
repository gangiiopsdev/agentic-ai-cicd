from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize input
    if not host or not host.isalnum():
        raise ValueError("Invalid hostname")
    return shlex.quote(host)

@app.get("/ping")
def ping(host: str):
    safe_host = safe_ping(host)
    subprocess.call(["ping", safe_host])

    return {"status": "completed"}