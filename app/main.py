from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['8.8.8.8', '127.0.0.1']:  # Allow only specific hosts
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"status": "denied"}