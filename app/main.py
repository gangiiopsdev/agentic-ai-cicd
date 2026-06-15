from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if host in ['127.0.0.1', 'localhost']:  # Example safe hosts
        subprocess.call(['ping', host])
    return {"status": "completed"}