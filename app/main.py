from fastapi import FastAPI
import subprocess
g import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using os.system with proper argument handling
    subprocess.call(['ping', host])
    return {"status": "completed"}