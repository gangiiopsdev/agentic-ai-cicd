from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError("Invalid host parameter")
    subprocess.call(["ping", host])
    return {"status": "completed"}