from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}