from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid input for host")

    safe_ping(host)

    return {"status": "completed"}