from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError('Invalid hostname')
    subprocess.call(["ping", host])
    return {"status": "completed"}