from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() for c in host):
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}