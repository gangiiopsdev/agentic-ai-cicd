from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    if not host:
        return False
    args = ['ping', '-c', '1', host]
    try:
        subprocess.run(args, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}