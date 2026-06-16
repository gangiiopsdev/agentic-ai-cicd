from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip().isalnum() and len(host.split('.')) == 4:
        subprocess.call(['ping', host])
    return {"status": "completed"}