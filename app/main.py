from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}