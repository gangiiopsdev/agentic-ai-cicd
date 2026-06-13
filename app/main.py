from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['example.com', 'test.net']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host) or not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}