from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    if host in ['google.com', 'github.com']:  # Example allowed hosts
        subprocess.call(['ping', host])
    else:
        return {"error": "Invalid host"}
    return {"status": "completed"}