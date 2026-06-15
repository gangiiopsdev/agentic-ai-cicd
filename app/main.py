from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and isinstance(host, str) and len(host.strip()) > 0:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input for ping"}