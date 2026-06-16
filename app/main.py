from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['localhost', '127.0.0.1']:  # Restrict allowed hosts
        subprocess.call(["ping", host])
    else:
        return {"status": "denied"}
    return {"status": "completed"}