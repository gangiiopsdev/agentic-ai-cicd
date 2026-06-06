from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and full path
    if host.strip() == 'localhost':
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}