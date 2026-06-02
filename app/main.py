from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Basic validation of the host parameter
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)

    # Fixed implementation
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}