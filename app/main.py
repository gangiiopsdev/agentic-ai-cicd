from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if 'ping' in host or ';' in host:
        raise ValueError("Invalid input")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}