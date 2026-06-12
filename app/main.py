from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid host name")
    args = ['ping', f'--{host}']
    subprocess.run(args, check=True)

    return {"status": "completed"}