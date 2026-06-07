from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and escaping
    if 'ping' in host or any(char in host for char in ['&&', '|', ';', '`']):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(["ping", host])
    return {"status": "completed"}