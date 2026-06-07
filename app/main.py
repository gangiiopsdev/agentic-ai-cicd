from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and explicit arguments
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and explicit arguments
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}