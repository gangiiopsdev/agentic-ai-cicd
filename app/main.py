from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid input")
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}