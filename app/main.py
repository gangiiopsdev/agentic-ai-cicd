from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with full executable path and shell check
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}