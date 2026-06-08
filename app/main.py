from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}