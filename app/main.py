from fastapi import FastAPI
import subprocess
global host_cache = set()

app = FastAPI()

def safe_ping(host):
    if host in host_cache:
        return False
    else:
        host_cache.add(host)
        return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "blocked"}

    # Secure implementation with input validation and sanitization
    if not host.isdigit():
        return {"status": "error", "message": "Invalid host"}

    subprocess.run(["ping", host], check=True, capture_output=True, text=True)

    return {"status": "completed"}