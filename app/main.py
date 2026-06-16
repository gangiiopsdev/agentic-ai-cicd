from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get="/ping")
def ping(host: str):    
    validate_host(host)
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}