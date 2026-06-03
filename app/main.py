from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return next((h for h in allowed_hosts if host == h), None)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}