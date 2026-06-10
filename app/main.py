from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation using subprocess.run with validation
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}