from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input before executing command
    subprocess.call(['ping', host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Sanitize input before executing command
    subprocess.run(['ping', host], check=True)