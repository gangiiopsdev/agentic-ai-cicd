from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}