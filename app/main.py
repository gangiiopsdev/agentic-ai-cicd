from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host in ('127.0.0.1', '::1'):  # Allow only local hosts for demonstration purposes
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
    return {"status": "completed"}