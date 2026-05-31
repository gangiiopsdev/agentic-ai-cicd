from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid input")
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}