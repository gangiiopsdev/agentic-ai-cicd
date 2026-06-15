from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['localhost', '127.0.0.1']:  # Whitelist allowed hosts
        subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}