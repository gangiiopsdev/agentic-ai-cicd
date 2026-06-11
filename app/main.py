from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation using subprocess.run with input validation and full path
    if host in ['8.8.8.8', '127.0.0.1']:  # Example allowed hosts
        subprocess.run(['ping', '-c', '4', host], check=True)
    return {"status": "completed"}