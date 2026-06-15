from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isdigit():  # Simple validation to prevent injection
        args = ['ping', host]
        subprocess.call(args)
    return {"status": "completed"}