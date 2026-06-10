from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Add logic to validate the host
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(["ping", host])
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}