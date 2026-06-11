from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith(('192.168.', '10.', '172.')):
        subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid host address")
    return {"status": "completed"}