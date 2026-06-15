from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or len(host) > 64:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}