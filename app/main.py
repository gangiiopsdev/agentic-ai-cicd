from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if host.strip() in ['localhost', '127.0.0.1']:
        subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    else:
        raise ValueError("Invalid host")

    return {"status": "completed"}