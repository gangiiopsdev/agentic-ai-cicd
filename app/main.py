from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with proper validation
    if host and isinstance(host, str) and not any(char in host for char in [';', '&', '|', '<', '>', '`']):
        subprocess.run(['ping', host], check=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with proper validation
    if host and isinstance(host, str) and not any(char in host for char in [';', '&', '|', '<', '>', '`']):
        subprocess.run(['ping', host], check=True)
    return {"status": "completed"}