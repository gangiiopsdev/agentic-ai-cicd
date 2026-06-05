from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.startswith('127.0.0.1') and not host.startswith('localhost'):
        return {'status': 'denied'}
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}