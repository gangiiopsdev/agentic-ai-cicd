from fastapi import FastAPI
import subprocess
cimport socket
def safe_ping(host: str):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "failed", "reason": "Invalid host"}