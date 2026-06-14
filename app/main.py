from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid host")

    return {"status": "completed"}