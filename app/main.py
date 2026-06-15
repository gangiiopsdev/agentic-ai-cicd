from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with additional validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.call(['ping', host])
    return {"status": "completed"}