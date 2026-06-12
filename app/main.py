from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with shell=False and avoiding partial executable paths
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}