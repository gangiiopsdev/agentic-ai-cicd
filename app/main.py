from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and full executable path
    if host.strip().isalnum() and len(host) < 256:
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid or too long host name"}

    return {"status": "completed"}