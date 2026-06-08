from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host.strip() or len(host) > 255:
        raise ValueError("Invalid hostname")
    subprocess.call(['ping', shlex.quote(host)])
    return {"status": "completed"}