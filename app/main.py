from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    if host.isalnum():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid hostname')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}