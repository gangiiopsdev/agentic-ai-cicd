from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return host in allowed_hosts