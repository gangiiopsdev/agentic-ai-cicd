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
    subprocess.run(['ping', '-c', '1', safe_host], check=True, text=True)
    return {"status": "completed"}