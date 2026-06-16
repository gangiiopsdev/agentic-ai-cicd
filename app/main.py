from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(["ping", host], check=True, capture_output=True)

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    return {"status": "completed", "message": safe_ping(host)}