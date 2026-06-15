from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)
    return {"status": "completed"}