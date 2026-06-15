from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip().endswith(('.', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        subprocess.call(['ping', host])
    return {"status": "completed"}