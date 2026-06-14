from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not host or not all(c.isalnum() for c in host):  # Allow only alphanumeric characters and some symbols like '.' and '-' for IP addresses
        raise ValueError('Invalid host parameter')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}