from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['127.0.0.1', 'localhost']:
        subprocess.run(["ping", host], check=True)
    else:
        return {"status": "error", "message": "Invalid host"}
    return {"status": "completed"}