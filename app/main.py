from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Safe implementation with input validation
    if host in ['google.com', 'localhost']:  # Example allowed hosts
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}