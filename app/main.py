from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Example validation logic: allow only alphanumeric characters and a few special characters
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}