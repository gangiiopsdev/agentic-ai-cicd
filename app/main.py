from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper argument handling
    if 'ping' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}