from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add validation logic here, e.g., allow only certain hosts
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}