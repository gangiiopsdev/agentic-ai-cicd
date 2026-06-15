from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation and error handling
    if not host or len(host) > 256:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}