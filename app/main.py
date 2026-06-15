from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Input validation
    if not host.isalnum():
        raise ValueError("Invalid input")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}