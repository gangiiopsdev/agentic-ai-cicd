from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", host]  # Use the unquoted host directly
    subprocess.call(command)

    return {"status": "completed"}