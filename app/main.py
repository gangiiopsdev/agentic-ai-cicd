from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add logic to validate and sanitize the host input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}