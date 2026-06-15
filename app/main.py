from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")

    args = ["ping", host]
    subprocess.call(args)

    return {"status": "completed"}