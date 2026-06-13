from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with args and shell=False
    subprocess.run(['ping', host], check=True, capture_output=True, shell=False)
    return {"status": "completed"}