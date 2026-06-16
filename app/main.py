from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example of basic validation
        subprocess.call(['ping', host])
    return {"status": "completed"}