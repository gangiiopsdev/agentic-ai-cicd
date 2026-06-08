from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in [allowed_host for allowed_host in os.listdir('/usr/local/bin/')]:
        raise Exception("Invalid host")
    subprocess.call(['ping', host])
    return {"status": "completed"}