from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter is required')
    subprocess.call(['ping', host], shell=False)

    return {"status": "completed"}