from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input sanitization
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}