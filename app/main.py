from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.isnumeric() or (host.startswith(".") and host.count(".") == 1):
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host format"}

    return {"status": "completed"}