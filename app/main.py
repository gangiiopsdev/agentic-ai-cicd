from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' not in host and '-' not in host:
        subprocess.call(['ping', f'-c 1 {host}'], shell=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if 'ping' not in host and '-' not in host:
        safe_ping(host)
    return {"status": "completed"}