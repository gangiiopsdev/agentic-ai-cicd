from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and list of arguments
    sanitized_host = host.replace(';', '')  # Simple sanitization example
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    return {"status": "completed"}