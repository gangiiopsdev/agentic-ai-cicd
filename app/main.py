from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '..' in host:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}