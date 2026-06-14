from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if host in ['127.0.0.1', '::1']:  # Example allowed IPs
        args = ['ping', host]
        subprocess.call(args)
    return {"status": "completed"}