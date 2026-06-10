from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Safe implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}