from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.isdigit() and len(host) == 3:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid host input"}
    return {"status": "completed"}