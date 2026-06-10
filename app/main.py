from fastapi import FastAPI
import subprocess
import os
def validate_host(host):
    allowed_hosts = [allowed_host for allowed_host in os.listdir('/usr/local/bin/')]
    if host not in allowed_hosts:
        raise Exception("Invalid host")

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], shell=False, check=True)
    return {"status": "completed"}