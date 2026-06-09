from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using Popen instead of call with shell=True
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}