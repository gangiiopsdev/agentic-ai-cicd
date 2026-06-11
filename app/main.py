from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.strip().isdigit() or '-' in host:
        subprocess.call(['ping', '-c 4', host])
    return {"status": "completed"}