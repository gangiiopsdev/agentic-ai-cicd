from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if 'ping' in host:
        subprocess.call(["ping", host])
    else:
        raise ValueError('Invalid command')
    return {"status": "completed"}