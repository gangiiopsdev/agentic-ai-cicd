from fastapi import FastAPI
import subprocess
from typing import List

global_hosts = {'example.com'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        subprocess.call(["ping", host])
    else:
        return {"status": "Invalid host"}
    return {"status": "completed"}