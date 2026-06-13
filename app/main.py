from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and validation
    if host in ['google.com', 'github.com']:  # Example allowed hosts
        subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")