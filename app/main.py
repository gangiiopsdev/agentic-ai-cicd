from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and list arguments
    safe_host = host.strip().replace(' ', '_')  # Basic sanitization
    if not safe_host.isalnum():
        raise ValueError("Invalid input")
    subprocess.run(["ping", safe_host], check=True)
    return {"status": "completed"}