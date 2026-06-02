from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    ping(host)
    return {"status": "completed"}