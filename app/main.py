from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation using subprocess.run with args and validation
    if not host.strip().replace('.', '').isdigit():
        raise ValueError("Invalid host address")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}