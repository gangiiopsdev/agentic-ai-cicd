from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list arguments
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in hostname')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}