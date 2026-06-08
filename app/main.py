from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input to prevent code injection
    if not host.strip().isalnum():
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)