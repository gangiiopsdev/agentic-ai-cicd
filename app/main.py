from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate host input (e.g., allow only alphanumeric characters and periods)
    if not all(c.isalnum() or c == '.' for c in host):
        raise ValueError("Invalid host")
    # Use subprocess.run instead of subprocess.call to improve safety
    subprocess.run(["ping", host], check=True, capture_output=True, text=True)

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}