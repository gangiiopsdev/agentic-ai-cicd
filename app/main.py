from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ('127.0.0.1', '::1'):  # Allow only local hosts
        subprocess.call(['ping', host])
    return {"status": "completed"}