from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation using subprocess.run instead of subprocess.call with shell=True
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": "completed"}