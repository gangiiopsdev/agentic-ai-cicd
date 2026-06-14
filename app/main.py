from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}