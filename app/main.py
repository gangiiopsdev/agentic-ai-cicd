from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}