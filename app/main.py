from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with full path and shell=True for demonstration purposes
    subprocess.call(['ping', host], shell=True)
    return {"status": "completed"}