from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Simple sanitization example, replace with proper validation logic
    return host.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}