from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or 'ping' in host:
        return {"error": "Invalid host"}
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)