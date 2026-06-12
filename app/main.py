from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"error": "Invalid input"}, 400
    # Secure implementation
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}