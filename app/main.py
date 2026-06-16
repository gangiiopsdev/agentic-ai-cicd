from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input
    if not host.isalnum():
        raise ValueError("Invalid host input")
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}