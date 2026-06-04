from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    safe_host = subprocess.quote(host)
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}