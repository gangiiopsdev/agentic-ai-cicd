from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid input"}, 400

    # Use subprocess.run with shell=False and proper argument handling
    subprocess.run(["ping", host], check=True)

    return {"status": "completed"}