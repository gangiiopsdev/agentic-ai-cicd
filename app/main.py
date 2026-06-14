from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation
    if host.isalnum():
        subprocess.run(["ping", host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host name")