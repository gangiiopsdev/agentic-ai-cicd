from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}