from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts here
    return host if host in allowed_hosts else None

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_host(host)
    if sanitized_host is not None:\n        subprocess.call(["ping", sanitized_host])\n        return {"status": "completed"}\n    else:\n        return {"status": "invalid host"}