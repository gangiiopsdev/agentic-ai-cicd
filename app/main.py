from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}