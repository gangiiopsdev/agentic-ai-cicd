from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with validation
    if all(c.isalnum() or c in ('.', '-') for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host name')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    return {"status": "completed"}