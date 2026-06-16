from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Sanitize the input to prevent shell injection
    if not host.isalnum() and not '.' in host:
        raise ValueError("Invalid host name")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}