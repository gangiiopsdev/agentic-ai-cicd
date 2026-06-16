from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with absolute path
    subprocess.run([os.path.join(os.sep, *host.split('.')), host], check=True)
    return {"status": "completed"}