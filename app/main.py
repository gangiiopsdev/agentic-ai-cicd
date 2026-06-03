from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation
    if not host.isdigit():
        return {"status": "failed", "message": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}