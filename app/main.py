from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation for demonstration purposes
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}