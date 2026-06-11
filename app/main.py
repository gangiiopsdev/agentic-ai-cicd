from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}