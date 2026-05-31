from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', '127.0.0.1']  # Replace with actual allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}, 403
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}