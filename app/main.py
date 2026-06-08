from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using os.system to avoid injection
    import os
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}