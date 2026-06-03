from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    if not host or not host.strip():
        raise ValueError("Invalid host provided")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}