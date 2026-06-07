from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() or c in [".", "-"] for c in host) and len(host) <= 255:
        subprocess.run(["ping", host], shell=False)
    else:
        return {"error": "Invalid hostname"}

    return {"status": "completed"}