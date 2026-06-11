from fastapi import FastAPI
import subprocess
c import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation using os.system
    subprocess.call(["ping", host])
    return {"status": "completed"}