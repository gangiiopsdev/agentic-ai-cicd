from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if host in ("localhost", "127.0.0.1"):  # Whitelisted hosts
        subprocess.call(["ping", host], check=True)
    else:
        raise ValueError("Invalid or untrusted host")

    return {"status": "completed"}