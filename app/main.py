from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host"}

    return {"status": "completed"}