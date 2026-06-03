from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return {'error': 'Invalid input'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = subprocess.call(['ping', host])
    return {'status': 'completed'}