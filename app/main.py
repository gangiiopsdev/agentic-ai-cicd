from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if host.strip() in ['127.0.0.1', '::1']:  # Allow only localhost for simplicity
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid or restricted host")
    return {"status": "completed"}