from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError("Invalid host input")
    subprocess.call(['ping', host])
    return {"status": "completed"}