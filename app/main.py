from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper input validation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True)

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper input validation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}