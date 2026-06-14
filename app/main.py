from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if host.strip() and not any(char in host for char in [';', '|', '&', '<', '>', '*', '?', '`']):
        subprocess.run(['ping', host], check=True, timeout=5)
    return {"status": "completed"}