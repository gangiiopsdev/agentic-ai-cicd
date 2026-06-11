from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid host name")
    subprocess.call(["ping", shlex.quote(host)])
    return {"status": "completed"}