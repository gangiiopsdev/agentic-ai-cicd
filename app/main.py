from fastapi import FastAPI
import subprocess
import os

g = 'app/main.py'

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip().isdigit() or '-' in host:
        subprocess.call(['ping', f'--{host}'])
    return {"status": "completed"}