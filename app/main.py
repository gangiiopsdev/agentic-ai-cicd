from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping/{host}")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}