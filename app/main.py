from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", *shlex.split(host)]
    subprocess.call(command)

    return {"status": "completed"}