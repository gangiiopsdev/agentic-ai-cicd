from fastapi import FastAPI
import subprocess
def ping(host: str):
    gateway = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': gateway.stdout if gateway.returncode == 0 else gateway.stderr}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': result.stdout if result.returncode == 0 else result.stderr}