from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shell=False and validating input
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}