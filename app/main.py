from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host.isnumeric() or '.' not in host:
        raise ValueError("Invalid host address")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}