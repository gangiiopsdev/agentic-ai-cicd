from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "denied", "message": "Host not allowed"}