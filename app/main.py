from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if host and host.isalnum():
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid input"}