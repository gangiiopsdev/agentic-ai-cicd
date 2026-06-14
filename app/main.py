from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)