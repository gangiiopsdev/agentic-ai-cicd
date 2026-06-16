from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input and use subprocess.run
    if not host.strip().isalnum():
        return {'error': 'Invalid host input'}
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use subprocess.run
    if not host.strip().isalnum():
        return {'error': 'Invalid host input'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}