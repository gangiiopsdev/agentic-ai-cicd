from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")