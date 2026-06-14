from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Ensure host is sanitized before use in subprocess call
    if any(char in host for char in [';', '&', '|', '<', '>', '*', '?']):
        raise ValueError('Invalid characters in hostname')
    return host

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input sanitization
    sanitized_host = safe_ping(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}