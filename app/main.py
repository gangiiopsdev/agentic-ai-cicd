from fastapi import FastAPI
import subprocess
import os
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise Exception("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}