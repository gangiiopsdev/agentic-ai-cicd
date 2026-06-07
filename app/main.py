from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['google.com', 'example.com']:  # Add a whitelist of allowed hosts
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host"}
    
    return {"status": "completed"}