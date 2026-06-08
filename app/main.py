from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        if not host.startswith('127.0.0.1') and not host.startswith('localhost'):  # Restrict hosts to local network
            raise ValueError("Invalid host")
        subprocess.call(['ping', host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}