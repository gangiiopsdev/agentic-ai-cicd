from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError("Invalid host input")
    safe_ping(host)
    return {"status": "completed"}