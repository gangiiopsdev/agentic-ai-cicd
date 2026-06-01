from fastapi import FastAPI
import subprocess
import shlex
import os

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}