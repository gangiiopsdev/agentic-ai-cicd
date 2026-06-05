from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Improved check for localhost and local IPs
        args = ['ping', host]
        subprocess.call(args)
    return {"status": "completed"}