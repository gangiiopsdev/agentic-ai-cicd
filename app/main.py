from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if host in ['example.com', 'localhost']:
        subprocess.call(['ping', '-c', '1', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}