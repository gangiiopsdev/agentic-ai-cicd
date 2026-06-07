from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Implement proper sanitization logic here
    return host.strip()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}