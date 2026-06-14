from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Safe implementation with input validation
    if not host.strip() or ' ' in host:
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}