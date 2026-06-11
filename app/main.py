from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"}
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.replace(';', '').replace('&', '')  # Basic input sanitization
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}