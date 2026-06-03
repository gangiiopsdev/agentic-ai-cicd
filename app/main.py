from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Improved security implementation
    safe_host = host.replace(';', '').replace('&', '')  # Remove potentially dangerous characters
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}