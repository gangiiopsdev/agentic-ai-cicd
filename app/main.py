from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip().isdigit() or host.strip().replace('.', '', 1).isdigit():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}