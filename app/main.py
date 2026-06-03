from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host input
    return '.' in host and len(host.split('.')) == 4