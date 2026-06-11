from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with absolute path and shell=False
    subprocess.run([os.path.abspath('ping'), host], check=True, shell=False)
    return {"status": "completed"}