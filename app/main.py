from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}