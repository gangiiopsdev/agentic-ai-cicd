from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate user input to prevent command injection
    if not host.isdigit() and len(host) < 100:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')