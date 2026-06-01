from fastapi import FastAPI
import subprocess
def safe_ping(host):
    valid_hosts = ["example.com", "localhost"]
    if host in valid_hosts:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)