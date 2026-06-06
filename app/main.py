from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    if host and '@' not in host and '.' in host:
        subprocess.run(['ping', '-c', '4', host], check=True)
    else:
        raise ValueError('Invalid host input')

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping_fixed")
def ping_fixed(host: str):
    return {"status": "completed"}