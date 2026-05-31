from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Replace with actual allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])
    return {"status": "completed"}