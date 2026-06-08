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
    if 'localhost' in host or '127.0.0.1' in host:
        args = ["ping", host]
        subprocess.call(args)
    return {"status": "completed"}