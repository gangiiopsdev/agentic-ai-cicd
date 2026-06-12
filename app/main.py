from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" )
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host and host.isalnum():
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid input for host')
    return {"status": "completed"}