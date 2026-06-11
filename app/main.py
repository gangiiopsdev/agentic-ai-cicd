from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid hostname")
    command = ["ping", host]
    subprocess.call(command)
    return {"status": "completed"}