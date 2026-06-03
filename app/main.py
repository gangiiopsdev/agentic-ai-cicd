from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it only contains expected characters
    if not host.isalnum() or len(host) > 20:
        raise ValueError("Invalid host input")
    args = ['ping', '127.0.0.1']  # Use a fixed IP instead of user input
    subprocess.call(args)

    return {"status": "completed"}