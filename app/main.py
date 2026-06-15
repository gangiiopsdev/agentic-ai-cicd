from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip().isalnum() and '.' in host:
        subprocess.call(["ping", host])
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}