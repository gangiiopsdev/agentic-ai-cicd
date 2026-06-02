from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):

    if not is_valid_host(host):
        raise ValueError('Invalid host')

    subprocess.call(["ping", host])

    return {"status": "completed"}