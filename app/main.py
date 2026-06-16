from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise Exception("Invalid host")

    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}