from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with full executable path and shell=False
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
    return {"status": "completed"}