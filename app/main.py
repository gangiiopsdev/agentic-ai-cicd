from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate or sanitize the input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid input")
    subprocess.run(['ping', '-c 1', host], check=True, shell=False)
    return {"status": "completed"}