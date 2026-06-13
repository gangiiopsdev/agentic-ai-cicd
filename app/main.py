from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using a whitelist for allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']  # Add more if needed
    if host in allowed_hosts:
        subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}