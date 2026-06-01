from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    if not host.isalnum():
        return {"status": "invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)