from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure host is sanitized before use in subprocess call
    if any(char in host for char in [';', '&', '|', '<', '>', '*', '?']):
        raise ValueError('Invalid characters in hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    safe_ping(host)
    subprocess.call(["ping", host])
    return {"status": "completed"}