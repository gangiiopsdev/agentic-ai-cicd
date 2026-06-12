from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host name')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    return {"status": "completed"}