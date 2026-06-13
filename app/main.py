from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if 'ping' not in host:
        return False
    # Use subprocess.run with list of arguments to avoid shell=True
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid host"}
    return {"status": "completed"}