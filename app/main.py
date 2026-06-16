from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and '.' in host:
        subprocess.call(['ping', host])
    else:
        raise ValueError("Invalid host address")
    return {"status": "completed"}