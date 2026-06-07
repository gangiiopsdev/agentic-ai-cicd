from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = ["ping", host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}