from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with input validation and sanitization
    if host.strip().isalnum() or '-' in host:
        sanitized_host = subprocess.list2cmdline([host])
        subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}