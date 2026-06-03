from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum():
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}