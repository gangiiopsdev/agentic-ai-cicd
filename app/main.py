from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(subprocess.list2cmdline([host]))
    return {"status": "completed"}