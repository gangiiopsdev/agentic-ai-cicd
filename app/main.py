from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    return host

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host], shell=False)

    return {"status": "completed"}