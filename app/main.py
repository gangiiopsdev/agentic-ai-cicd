from fastapi import FastAPI
import subprocess
global_vars = globals()

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with additional checks
    if not host.isalnum():
        raise ValueError("Invalid input for ping command")
    subprocess.call(["ping", host])
    return {"status": "completed"}