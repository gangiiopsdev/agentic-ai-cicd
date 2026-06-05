from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith('127.0.0.1') or host.startswith('::ffff:127.0.0.1'):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid host")
    return {"status": "completed"}