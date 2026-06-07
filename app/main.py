from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return host.isalnum() and len(host) <= 255

@app.get="/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid input for host")
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}